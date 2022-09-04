"""
The purpose of this script is to extract data from the TEI file provided by grobid.
input: tei folder 
output: parquet file with columns ACL_id, title, abstract, full_text

to run - python main.py --path_to_extraction_folder /data/ACL.80k/grobid_out/
"""

from dataclasses import dataclass
from pathlib import Path
from bs4 import BeautifulSoup
import argparse
import glob
from tqdm import tqdm
import pandas as pd

tqdm.pandas()


def read_tei(tei_file):
    with open(tei_file, "r") as tei:
        soup = BeautifulSoup(tei, "lxml")
        return soup
    raise RuntimeError("Cannot generate a soup from the input")


def elem_to_text(elem, default=""):
    if elem:
        return elem.getText()
    else:
        return default


@dataclass
class Person:
    firstname: str
    middlename: str
    surname: str


class TEIFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.soup = read_tei(filename)
        self._text = None
        self._title = ""
        self._abstract = ""

    def basename(self):
        stem = Path(self.filename).stem
        if stem.endswith(".tei"):
            # Return base name without tei file
            return stem[0:-4]
        else:
            return stem

    @property
    def title(self):
        if not self._title and self.soup.title:
            self._title = self.soup.title.getText()
        return self._title

    @property
    def abstract(self):
        if not self._abstract and self.soup.abstract:
            abstract = self.soup.abstract.getText(separator=" ", strip=True)
            self._abstract = abstract
        return self._abstract

    @property
    def text(self):
        if not self._text:
            divs_text = []
            for div in self.soup.body.find_all("div"):
                # div is neither an appendix nor references, just plain text.
                if not div.get("type"):
                    div_text = div.get_text(separator=" ", strip=True)
                    divs_text.append(div_text)

            plain_text = " ".join(divs_text)
            self._text = plain_text
        return self._text


def get_dataframe(path_to_extraction_folder, k=None):
    list_files = glob.glob(path_to_extraction_folder + "*.tei.xml")
    df = pd.DataFrame(list_files[:k], columns=["path"])

    df["tei"] = df.progress_apply(
        lambda row: TEIFile(row["path"]),
        axis=1,
    )

    df["acl_id"] = df.progress_apply(
        lambda row: row["tei"].basename(),
        axis=1,
    )

    df["title"] = df.progress_apply(
        lambda row: row["tei"].title,
        axis=1,
    )

    df["abstract"] = df.progress_apply(
        lambda row: row["tei"].abstract,
        axis=1,
    )

    df["full_text"] = df.progress_apply(
        lambda row: row["tei"].text,
        axis=1,
    )

    df = df.drop(["tei", "path"], axis=1)
    df.to_parquet("acl_corpus_full-text.parquet", compression="gzip")

    return df


if __name__ == "__main__":
    data = []
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path_to_extraction_folder",
        type=str,
        required=True,
        default="",
        help="path to the grobid extraction folder which has the TEI files",
    )

    parser.add_argument(
        "--k",
        type=int,
        default=None,
        help="path to the grobid extraction folder which has the TEI files",
    )

    args = parser.parse_args()
    k = args.k

    df = get_dataframe(args.path_to_extraction_folder, k)
