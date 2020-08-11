#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Colin Chan
# Script to scrub content and condense data into one text file
# To use: Edit three constants for novel. Open text file in fbreader
# Depedencies: beautiful soup -> pip install beautifulsoup4

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os

DATA_SOURCE = "https://www.wuxiaworld.com/novel/rmji/rmji-chapter-"
NUM_CHAPTERS = 1629
WRITE_FILE = os.path.join(os.getcwd(), "rmji.txt")


def main():
    """ Main program """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
               'AppleWebKit/537.11 (KHTML, like Gecko) '
               'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

    if os.path.exists(WRITE_FILE):
        os.remove(WRITE_FILE)

    f = open(WRITE_FILE, "a")

    for i in range(NUM_CHAPTERS):
        # Retrieve raw HTML of current webpage
        data_source = DATA_SOURCE + str(i+1)
        req = Request(url=data_source, headers=headers)
        sample_data = urlopen(req).read()

        # Filter and format chapter contents
        # Warning: Chapter title location is not consistent.
        #          Title location can vary, different p/div tag
        # Todo: Find a more robust way to insert chapter title
        soup = BeautifulSoup(sample_data)
        content = soup.find(id="chapter-content")
        content = content.find_all('p')

        # Write chapter contents to text file
        for x in content:
            f.write(x.text + "\n\n")

        # Current status
        print("Page" + str(i))

    f.close()
    return 0


if __name__ == "__main__":
    main()
