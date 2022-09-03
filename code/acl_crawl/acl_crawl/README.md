# ACL Crawler


Contains the code for crawling a whole domain and getting all the links in that domain

Once you have the links - you can fetch the contents quickly

Runs with latest version of scrapy - `pip install scrapy`

For example here we demonstrate ACL crawling


1. ist441_bot/spiders/follow_spider.py

Edit the domain and start url if needed.

All links are saved in the file - `links_bib.txt`

to run this code type - `scrapy crawl geturl`

```
# replace .bib with .pdf
sed -i 's/.bib/.pdf/g' links_bib.txt

#  change file name
mv links_bib.txt links_pdf.txt 

# curl in parallel - 16 jobs : BE POLITE
parallel -j16 -k curl -O < links_pdf.txt
```

This will download all the 

