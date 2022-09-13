import nltk
import pandas as pd
from tqdm import tqdm
import random

df = pd.read_parquet("acl_corpus_full-text.parquet")

number_sentences = 6

data = []

for text in tqdm(df["full_text"]):
    sent_tokens = nltk.sent_tokenize(text)
    for i in range(0, len(sent_tokens), number_sentences):
        data.append(" ".join(sent_tokens[i : i + number_sentences]))

random.shuffle(data)
with open("train_sentences.txt", "w") as f:
    # for line in data[:1687922]:
    # f.write("%s\n" % line)
    f.write("\n".join(data[:1687922]))


with open("val_sentences.txt", "w") as f:
    f.write("\n".join(data[1687922:]))
