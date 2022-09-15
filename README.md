# ACL Anthology Corpus - Full Text 📚

[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This repository provides full-text and metadata to the ACL anthology collection (80k articles/posters as of September 2022) also including .pdf files and grobid extractions of the pdfs.

## How is this different from what ACL anthology provides and what already exists? 
- We provide pdfs, full-text, references and other details extracted by grobid from the PDFs while [ACL Anthology](https://aclanthology.org/anthology+abstracts.bib.gz) only provides abstracts. 
- There exists a similar corpus call [ACL Anthology Network](https://clair.eecs.umich.edu/aan/about.php) but is now showing its age with just 23k papers from Dec 2016.

----

The goal is to keep this corpus updated and provide a comprehensive repository of the full ACL collection.

This repository provides data for `80,013` ACL articles/posters - 
1. 📖 All PDFs in ACL anthology : **size 45G**  [download here](https://drive.google.com/file/d/1OGHyJrkaVpbrdbmxsDotG-tI3LiKyxuC/view?usp=sharing)
2. 🎓 All bib files in ACL anthology with abstracts : **size 172M** [download here](https://drive.google.com/file/d/1dJ-iE85moBv3iYG2LhRLT6KQyVkmllBg/view?usp=sharing)
2. 🏷️  Raw grobid extraction results on all the ACL anthology pdfs which includes full text and references : **size 3.6G** [download here](https://drive.google.com/file/d/1xC-K6__W3FCalIDBlDROeN4d4xh0IVry/view?usp=sharing)
3. 💾  Dataframe with metadata and full text of the collection for analysis : **size 503M** [download here](https://drive.google.com/file/d/19rEco5OT4Um-0DNzna27UfZ1wjSG5oKC/view?usp=sharing)

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

The API can be used to fetch more information for each paper in the corpus.

---
## Text generation on Huggingface

We fine-tuned the distilgpt2 model from huggingface using the full-text from this corpus. The model is trained for generation task.

Text Generation Demo : https://huggingface.co/shaurya0512/distilgpt2-finetune-acl22

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
Generated: We introduce a new language representation for the task of sentiment classification. We propose an approach to learn representations from   unlabeled data, which is based on supervised learning and can be applied in many applications such as machine translation (MT) or information retrieval   systems where labeled text has been used by humans with limited training time but no supervision available at all. Our method achieves state-oftheart   results using only one dataset per domain compared to other approaches that use multiple datasets simultaneously, including BERTScore(Devlin et al.,   2019; Liu & Lapata, 2020b ) ; RoBERTa+LSTM + L2SRC -  
``` 


TODO:
1. Link the acl corpus to semantic scholar(S2), sources like S2ORC 
2. Extract figures and captions from the ACL corpus using pdffigures.
3. Have a release schedule to keep the corpus updated.
4. ACL citation graph
5. Enhance metadata with bib file mapping - include authors
6. Add citation counts for papers

We are hoping that this corpus can be helpful for analysis relevant to the ACL community. 


**Please cite/star 🌟 this page if you use this corpus**

[<img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black">](https://www.buymeacoffee.com/shauryrG)

<!-- If you are feeling generous buy me a ☕   -->

## License

ACL anthology corpus is released under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).  By using this corpus, you are agreeing to its usage terms.
