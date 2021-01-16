# Jade Slip Replicator
Scrapes chapter contents to a text file. Consume using your favourite reader. 

# Usage
Capture and read in the first 100 chapters of light novel RMJI

* DATA_SOURCE = "https://www.wuxiaworld.com/novel/rmji/rmji-chapter-"
* NUM_CHAPTERS = 100
* WRITE_FILE = os.path.join(os.getcwd(), "rmji.txt")

# Dependencies: 
 * beautiful soup -> pip install beautifulsoup4
