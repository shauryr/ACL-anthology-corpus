#!/usr/bin/env python3

"""
Compute rudimentary dataset statistics such as sentence/word counts, valid examples and present languages.
"""

import pandas as pd
import argparse
import langdetect
import tqdm
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

args = argparse.ArgumentParser()
args.add_argument(
    "-d", "--data", default="data/acl-publication-info.74k.parquet",
    help="Path to the input parquet file."
)
args.add_argument(
    "-t", "--total", type=int, default=None,
    help="How many rows to consider (for fast development)."
)
args = args.parse_args()
data = pd.read_parquet(args.data)

unique_hash = set()
langs = []
sent_counts_abstract = []
word_counts_abstract = []
sent_counts_paper = []
word_counts_paper = []
word_counts_title = []
citedby_paper = []
author_counts_paper = []
pages_counts_paper = []

# main loop to aggregate stats
for row_i, row in tqdm.tqdm(
    data[:args.total].iterrows(),
    total=args.total if args.total is not None else data.shape[0]
):
    # if any row has title/abstract/full_text empty, consider it invalid
    if len(row["title"].strip()) == 0 or len(row["abstract"].strip()) == 0 or len(row["full_text"].strip()) == 0:
        continue

    # disregard all papers if they have the same title and abstract
    row_hash = f'{row["title"]} ||| {row["abstract"]}'
    if row_hash in unique_hash:
        continue
    unique_hash.add(row_hash)

    # detect and store language
    lang_abstract = langdetect.detect(row["abstract"])
    langs.append(lang_abstract)

    # Fulltext starts with the abstract. We can either assume that all paper texts start with "Introduction"
    # (which is false in general) or just use the offset of the abstract.
    fulltext_without_abstract = row["full_text"][len(row["abstract"]):]

    # store sent/word counts
    sent_counts_abstract.append(len(sent_tokenize(row["abstract"])))
    word_counts_abstract.append(len(word_tokenize(row["abstract"])))
    sent_counts_paper.append(len(sent_tokenize(fulltext_without_abstract)))
    word_counts_paper.append(len(word_tokenize(fulltext_without_abstract)))
    word_counts_title.append(len(word_tokenize(row["title"])))
    citedby_paper.append(row["numcitedby"])

    # sometimes authors are not available
    if row["author"] is not None:
        author_counts_paper.append(row["author"].count(" and") + 1)

    # attempt to parse pages span
    if row["pages"] is not None and "--" in row["pages"]:
        pages = row["pages"].split("--")
        try:
            page_l = int(pages[0])
            page_r = int(pages[1])
            pages_total = page_r - page_l + 1
            pages_counts_paper.append(pages_total)
        except:
            pass

# print all stats
print("Langs:", ", ".join([
    f"{l} {v} ({v/len(unique_hash):.1%})"
    for l, v in Counter(langs).most_common()
]))
print(f'{"Total:":>40}', data.shape[0])
print(f'{"Total unique & valid:":>40}', len(unique_hash))
print(
    f'{"Average sents (words) per abstract:":>40}',
    f"{np.average(sent_counts_abstract):.1f} ({np.average(word_counts_abstract):.1f})"
)
print(
    f'{"Average sents (words) per paper:":>40}',
    f"{np.average(sent_counts_paper):.1f} ({np.average(word_counts_paper):.1f})"
)
print(
    f'{"Average words/title:":>40}',
    f"{np.average(word_counts_title):.1f}"
)
print(
    f'{"Total sents (words):":>40}',
    f"{sum(sent_counts_abstract) + sum(sent_counts_paper)} ({sum(word_counts_abstract) + sum(word_counts_paper)})"
)
print(
    f'{"Average number of authors:":>40}',
    f"{np.average(author_counts_paper):.1f}"
)
print(
    f'{"Average number of citations:":>40}',
    f"{np.average(citedby_paper):.1f}"
)
print(
    f'{"Average number of pages per paper:":>40}',
    f"{np.average(pages_counts_paper):.1f}"
)
