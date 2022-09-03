# ACL Anthology Corpus - Full Text 📚
This repository provides full-text and metadata to the ACL anthology collection including .pdf files and grobid extractions of the pdfs.

## How is this different from what ACL anthology provides? 
We are also providing full-text, references and other details extracted by grobid from the PDFs. If you just want abstracts, please visit - [acl anthology](https://aclanthology.org/anthology+abstracts.bib.gz) 


----

The goal is to keep this repo updated and provide a comprehensive repository of the full ACL collection.

This repository provides data for `80,015` ACL articles - 
1. 📖 All PDFs in ACL anthology : **size 45G**  [download here](https://drive.google.com/file/d/1OGHyJrkaVpbrdbmxsDotG-tI3LiKyxuC/view?usp=sharing)
2. All bib files in ACL anthology with abstracts : **size 172M** [download here](https://drive.google.com/file/d/1dJ-iE85moBv3iYG2LhRLT6KQyVkmllBg/view?usp=sharing)
2. 🏷️ Raw grobid extraction results on all the ACL anthology pdfs which includes full text and references [TODO]
3. 💾 CSV file with metadata and full text of the collection for analysis 

```python
>>> import pandas as pd
>>> pd.read_parquet('acl_corpus_full-text.parquet')

            acl_id           title        abstract       full_text
0         P83-1025  Discourse P...  This paper ...  This paper ...
1         P93-1015  Parsing Fre...  There is a ...  There is a ...
2         P82-1017  REFLECTIONS...                  Our society...
3         C86-1129  A Lexical F...  This paper ...  This paper ...
4         C80-1093  AUTHOR INDE...                                
..             ...             ...             ...             ...
95  2022.hcinlp...                                  Introductio...
96   2021.tacl-1.9  On the Rela...  We use larg...  We use larg...
97  2022.nlp4co...  Understandi...  Exemplar-ba...  Exemplar-ba...
98  2022.nlp4co...  Stylistic R...  Personality...  Personality...
99  2022.nlp4co...  Toward Know...  Conversatio...  Conversatio...
```

The  provided ACL id is consistent with S2 API as well - 

[https://api.semanticscholar.org/graph/v1/paper/ACL:P83-1025](https://api.semanticscholar.org/graph/v1/paper/ACL:P83-1025)



TODO:
1. Link the acl corpus to semantic scholar(S2), sources like S2ORC 
2. Extract figures and captions from the ACL corpus using pdffigures.
3. Have a release schedule to keep the corpus updated.
4. ACL citation graph
5. Enhance metadata with bib file mapping

We are hoping that this corpus can be helpful for analysis relevant to the ACL community. 

Please cite/star 🌟 this page if you use this corpus.

[<img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black">](https://www.buymeacoffee.com/shauryrG)

If you are feeling generous buy me a ☕  