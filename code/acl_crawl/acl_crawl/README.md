# ACL Crawler


Contains the code for crawling a whole domain and getting all the links in that domain

Once you have the links - you can fetch the contents quickly

Runs with latest version of scrapy - `pip install scrapy`

For example here we demonstrate ACL crawling


1. acl_crawl/spiders/follow_spider.py

Edit the domain and start url if needed.

All links are saved in the file - `links_bib.txt`

to run this code type - `scrapy crawl geturl`


```bash
# replace .bib with .pdf
sed -i 's/.bib/.pdf/g' links_bib.txt
```

```bash
# for macos 
sed -i '' 's/\.bib/\.pdf/g' links_bib.txt 
```

```bash
#  change file name
mv links_bib.txt links_pdf.txt 
```

```bash
# curl in parallel - 16 jobs : BE POLITE
parallel -j16 -k curl -O < links_pdf.txt
```

This will download all the pdfs from ACL.

## Fetching new papers

Fetch the pdf links using the above code.

Then get the new papers - 

```bash
comm -13 <(sort links_pdf.2022.txt) <(sort links_pdf.2023.txt)
```

- The `-13` option to `comm` suppresses lines unique to FILE1 (`-1`) and lines that appear in both files (`-3`).
- The `<()` syntax is a bash feature known as process substitution, that lets a process's output be used as an input file for another process.

This command will display lines that only appear in `links_pdf.2023.txt`, i.e., the new lines in 2023 file and not in 2022 file.


Now crawl the delta -

```bash
parallel -j8 -k curl -O < ../acl_crawl/links_delta.pdf.2023.txt
```