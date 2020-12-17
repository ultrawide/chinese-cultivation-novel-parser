###########################################################
# Scrape and condense chapter contents into a text file
# To use: Edit the three constants as per novel.
# Dependencies: beautiful soup -> pip install beautifulsoup4
###########################################################

import os
import io
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

DATA_SOURCE = "https://www.wuxiaworld.com/novel/rmji/rmji-chapter-"
NUM_CHAPTERS = 20
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

    with io.open(WRITE_FILE, "a", encoding="utf-8") as f:
        for chapter in range(1, NUM_CHAPTERS):
            # Retrieve raw HTML of current webpage
            data_source = DATA_SOURCE + str(chapter)
            req = Request(url=data_source, headers=headers)
            sample_data = urlopen(req).read()

            # Filter and format chapter contents
            # Warning: Chapter information tag is not consistent
            # Todo: Need robust method to insert chapter title information
            soup = BeautifulSoup(sample_data)
            content = soup.find(id="chapter-content")
            content = content.find_all('p')

            # Write chapter contents to text file
            for x in content:
                f.write(x.text + "\n\n")

            # Current status
            print("Page" + str(chapter))

if __name__ == "__main__":
    main()
