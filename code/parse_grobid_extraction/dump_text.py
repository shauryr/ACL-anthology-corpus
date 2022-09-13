import pandas as pd
import numpy as np

df = pd.read_parquet("acl_corpus_full-text.parquet")


df["full_text"][:70000].to_csv('train.txt', sep='\t', index=False)

df["full_text"][70000:].to_csv('val.txt', sep='\t', index=False)