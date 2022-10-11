# 📚  ACL Anthology Corpus - Full Text

[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This repository provides full-text and metadata to the ACL anthology collection (80k articles/posters as of September 2022) also including .pdf files and grobid extractions of the pdfs.

## How is this different from what ACL anthology provides and what already exists?

- We provide pdfs, full-text, references and other details extracted by grobid from the PDFs while [ACL Anthology](https://aclanthology.org/anthology+abstracts.bib.gz) only provides abstracts.
- There exists a similar corpus call [ACL Anthology Network](https://clair.eecs.umich.edu/aan/about.php) but is now showing its age with just 23k papers from Dec 2016.

----

The goal is to keep this corpus updated and provide a comprehensive repository of the full ACL collection.

This repository provides data for `73,285` ACL articles/posters -

1. 📖 All PDFs in ACL anthology : **size 45G**  [download here](https://drive.google.com/file/d/1OGHyJrkaVpbrdbmxsDotG-tI3LiKyxuC/view?usp=sharing)
2. 🎓 All bib files in ACL anthology with abstracts : **size 172M** [download here](https://drive.google.com/file/d/1dJ-iE85moBv3iYG2LhRLT6KQyVkmllBg/view?usp=sharing)
3. 🏷️  Raw grobid extraction results on all the ACL anthology pdfs which includes full text and references : **size 3.6G** [download here](https://drive.google.com/file/d/1xC-K6__W3FCalIDBlDROeN4d4xh0IVry/view?usp=sharing)
4. 💾  Dataframe with extracted metadata (table below with details) and full text of the collection for analysis : **size 489M** [download here](https://drive.google.com/file/d/1CFCzNGlTls0H-Zcaem4Hg_ETj4ebhcDO/view?usp=sharing)

|  **Column name**   |        **Description**        |
| :----------------: | :---------------------------: |
|     `acl_id`      |         unique ACL id         |
|    `abstract`     | abstract extracted by GROBID  |
|    `full_text`    | full text extracted by GROBID |
| `corpus_paper_id` |      Semantic Scholar ID      |
|    `pdf_hash`     |     sha1 hash of the pdf      |
|   `numcitedby`    |  number of citations from S2  |
|       `url`       |      link of publication      |
|    `publisher`    |               -               |
|     `address`     |     Address of conference     |
|       `year`       |               -               |
|      `month`      |               -               |
|    `booktitle`    |               -               |
|     `author`      |        list of authors        |
|      `title`      |        title of paper         |
|      `pages`      |               -               |
|       `doi`       |               -               |
|     `number`      |               -               |
|     `volume`      |               -               |
|     `journal`     |               -               |
|     `editor`      |               -               |
|      `isbn`       |               -               |

```python
>>> import pandas as pd
>>> df = pd.read_parquet('acl-publication-info.74k.parquet')
>>> df
         acl_id                                           abstract                                          full_text  corpus_paper_id                                  pdf_hash  ...  number volume journal editor  isbn
0      O02-2002  There is a need to measure word similarity whe...  There is a need to measure word similarity whe...         18022704  0b09178ac8d17a92f16140365363d8df88c757d0  ...    None   None    None   None  None
1      L02-1310                                                                                                                8220988  8d5e31610bc82c2abc86bc20ceba684c97e66024  ...    None   None    None   None  None
2      R13-1042  Thread disentanglement is the task of separati...  Thread disentanglement is the task of separati...         16703040  3eb736b17a5acb583b9a9bd99837427753632cdb  ...    None   None    None   None  None
3      W05-0819  In this paper, we describe a word alignment al...  In this paper, we describe a word alignment al...          1215281  b20450f67116e59d1348fc472cfc09f96e348f55  ...    None   None    None   None  None
4      L02-1309                                                                                                               18078432  011e943b64a78dadc3440674419821ee080f0de3  ...    None   None    None   None  None
...         ...                                                ...                                                ...              ...                                       ...  ...     ...    ...     ...    ...   ...
73280  P99-1002  This paper describes recent progress and the a...  This paper describes recent progress and the a...           715160  ab17a01f142124744c6ae425f8a23011366ec3ee  ...    None   None    None   None  None
73281  P00-1009  We present an LFG-DOP parser which uses fragme...  We present an LFG-DOP parser which uses fragme...          1356246  ad005b3fd0c867667118482227e31d9378229751  ...    None   None    None   None  None
73282  P99-1056  The processes through which readers evoke ment...  The processes through which readers evoke ment...          7277828  924cf7a4836ebfc20ee094c30e61b949be049fb6  ...    None   None    None   None  None
73283  P99-1051  This paper examines the extent to which verb d...  This paper examines the extent to which verb d...          1829043  6b1f6f28ee36de69e8afac39461ee1158cd4d49a  ...    None   None    None   None  None
73284  P00-1013  Spoken dialogue managers have benefited from u...  Spoken dialogue managers have benefited from u...         10903652  483c818c09e39d9da47103fbf2da8aaa7acacf01  ...    None   None    None   None  None

[73285 rows x 21 columns]
```

The  provided ACL id is consistent with S2 API as well -

[https://api.semanticscholar.org/graph/v1/paper/ACL:P83-1025](https://api.semanticscholar.org/graph/v1/paper/ACL:P83-1025)

The API can be used to fetch more information for each paper in the corpus.

---

## Dataset Statistics

<!-- Run code/statistics/main.py to get information for this table -->

- **Total rows**: 73285
- **Total unique & valid rows**: 63422
- **Language distribution**: en 62308 (96.5%), fr 2037 (3.2%), pt 54 (0.1%), cy 25, ca 17, fi 14, no 11, de 10, ko 10, ... (long tail of less-represented languages)
- **Average sents (words) per abstract**: 5.7 (140.5)
- **Average sents (words) per paper text**: 159.0 (4264.7)
- **Average words per title**: 10.4
- **Total sents/words**: 11mil (284mil)
- **Average number of authors**: 3.2
- **Average number of citations**: 35.4
- **Average number of pages per paper**: 9.2

## Text generation on Huggingface

We fine-tuned the distilgpt2 model from huggingface using the full-text from this corpus. The model is trained for generation task.

Text Generation Demo : <https://huggingface.co/shaurya0512/distilgpt2-finetune-acl22>

Example:

```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM
>>> tokenizer = AutoTokenizer.from_pretrained("shaurya0512/distilgpt2-finetune-acl22")
>>> model = AutoModelForCausalLM.from_pretrained("shaurya0512/distilgpt2-finetune-acl22")
>>>
>>> input_context = "We introduce a new language representation"
>>> input_ids = tokenizer.encode(input_context, return_tensors="pt")  # encode input context
>>> outputs = model.generate(
...     input_ids=input_ids, max_length=128, temperature=0.7, repetition_penalty=1.2
... )  # generate sequences
>>> print(f"Generated: {tokenizer.decode(outputs[0], skip_special_tokens=True)}")
```

```text
Generated: We introduce a new language representation for the task of sentiment classification. We propose an approach to learn representations from   
unlabeled data, which is based on supervised learning and can be applied in many applications such as machine translation (MT) or information retrieval   
systems where labeled text has been used by humans with limited training time but no supervision available at all. Our method achieves state-oftheart   
results using only one dataset per domain compared to other approaches that use multiple datasets simultaneously, including BERTScore(Devlin et al.,   
2019; Liu & Lapata, 2020b ) ; RoBERTa+LSTM + L2SRC -  
```

### TODO

1. ~~Link the acl corpus to semantic scholar(S2), sources like S2ORC~~
2. Extract figures and captions from the ACL corpus using pdffigures - [scientific-figure-captioning](https://github.com/billchen0/scientific-figure-captioning)
3. Have a release schedule to keep the corpus updated.
4. ACL citation graph
5. ~~Enhance metadata with bib file mapping - include authors~~
6. ~~Add citation counts for papers~~
7. Use [ForeCite](https://github.com/allenai/ForeCite) to extract impactful keywords from the corpus
8. Link datasets using [paperswithcode](https://github.com/paperswithcode/paperswithcode-data)? - don't know how useful this is
9. Have some stats about the data - [linguistic-diversity](http://stats.aclrollingreview.org/submissions/linguistic-diversity/); [geo-diversity](http://stats.aclrollingreview.org/submissions/geo-diversity/); if possible [explorer](http://stats.aclrollingreview.org/submissions/explorer/)

We are hoping that this corpus can be helpful for analysis relevant to the ACL community.

**Please cite/star 🌟 this page if you use this corpus**

## Citing the ACL Anthology Corpus

If you use this corpus in your research please use the following BibTeX entry:

    @Misc{acl_anthology_corpus,
        author =       {Shaurya Rohatgi},
        title =        {ACL Anthology Corpus with Full Text},
        howpublished = {Github},
        year =         {2022},
        url =          {https://github.com/shauryr/ACL-anthology-corpus}
    }

[<img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black">](https://www.buymeacoffee.com/shauryrG)

<!-- If you are feeling generous buy me a ☕   -->

## Acknowledgements

We thank Semantic Scholar for providing access to the citation related data in this corpus.

## License

ACL anthology corpus is released under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  By using this corpus, you are agreeing to its usage terms.
