## Existing Datasets


1. [ACL Anthology Network (AAN)](https://clair.eecs.umich.edu/aan/about.php), 2013 

[Paper](https://aclanthology.org/W09-3607.pdf)

Summary :
- How they did it?
    -  13,739 papers
    - PDFBOX to extract information

- What they did - novelty ?
    - Semi manual annotation of references 
    - provide citation contexts : sentences around where a paper was cited 
    - Manual gender annotation
    - related phrases for every author using the text from the papers they have authored (basic tf-idf)
    - a lot of graph/network statistics like out-degree analysis

-----
2. [ACL Anthology Reference Corpus ARC](https://www.sketchengine.eu/acl-anthology-reference-corpus-arc/), 2016

[arxive link](https://web.archive.org/web/20160304175530/https://acl-arc.comp.nus.edu.sg/)

[Short Paper](http://www.lrec-conf.org/proceedings/lrec2008/pdf/445_paper.pdf)

- How they did it?
    - 10,921 pdfs - 2007 version
    - ???? pdfs - 2016 version
    - PDFBOX

- What they did - novelty?
    - inter and intra reference linking
    - proposed a task for benchmarking the above



3. Corpling@GU (Georgetown University) have ACL Anthology from 1985-2022  - Behind firewall


Other work using these datasets/similar work- 

1. [Citation Analysis, Centrality, and the ACL Anthology](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.125.9410&rep=rep1&type=pdf)
Detailed citation network analysis. They even list which paper has most citation inside the network which would be good to see. The work also calculates the impact factor of ACL anthology which is interesting.

2. [Purpose and Polarity of Citation: Towards NLP-based Bibliometrics](https://aclanthology.org/N13-1067.pdf) 
This might of interest to folks working in citation context classification.

3.  [CORD-19: The COVID-19 Open Research Dataset](https://www.semanticscholar.org/reader/4a10dffca6dcce9c570cb75aa4d76522c34a2fd4)
This paper can be a template for the work we are doing. It is very similar to what we are doing but in ACL domain. We can take inspiration and do stuff tailored for the linguistics community. Tasks mentioned in section 4 `Research directions` are specially very iteresting for us.

There are mostly summarization tasks around AAN - using the citation context given by the dataset.

