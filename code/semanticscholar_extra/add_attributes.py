"""
TODO
"""

import pandas as pd
import semanticscholar
import argparse

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument(
        "-di", "--data-in", default="data/acl_corpus_full-text.parquet",
        help="Path to the input parquet file."
    )
    args.add_argument(
        "-f", "--feature", nargs="+",
        default=["url", "citation_count", "citations", "references", "authors", "year"],
    )
    args.add_argument(
        "-do", "--data-out", default="data/acl_corpus_full-text-ss.parquet",
        help="Path to the output parquet file."
    )
    args = args.parse_args()

    data = pd.read_parquet(args.data_in)
    print(data.describe())