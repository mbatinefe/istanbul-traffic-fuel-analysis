'''
# PY FILE NUMBER 1

This python algorithm will be requesting data from IBB traffic.
That requested data will be our "download links" for each month and for each year.

Creates: ibb_links.txt
Problem: NaN

'''


import os, sys, glob, re
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import uuid

LINK_LIST_PATH = 'ibb_links.txt'

# Encoding for writing the URLs to the .txt file
# Do not change unless you are getting a UnicodeEncodeError
ENCODING = "utf-8"


def save_link(url, date):

    # Save collected link/url and page to the .txt
    with open(LINK_LIST_PATH, "a", encoding=ENCODING) as f:
        f.write("\t".join([url, date]) + "\n")


def download_links_from_index():
    # Go to the defined "url" and download the page links
    # Checking if the link_list.txt file exists
    if not os.path.exists(LINK_LIST_PATH):
        with open(LINK_LIST_PATH, "w", encoding=ENCODING) as f:
            f.write("\t".join(["url", "date"]) + "\n")
        downloaded_url_list = []

    # If some links have already been downloaded,
    # get the downloaded links and start page
    else:
        data = pd.read_csv(LINK_LIST_PATH, sep="\t")
        if data.shape[0] == 0:
            downloaded_url_list = []
        else:
            downloaded_url_list = data["url"].to_list()

        # time you ran the code (if you had an error and the code stopped)

    pageURL = 'https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set'

    resp = requests.get(pageURL)
    soup = bs(resp.content, 'html.parser')

    for item in soup.find_all('li', {'class': 'resource-item'}):
        url = item.find('div', {'class': 'data-name'}).find('a')['href']
        date = item.find('div', {'class': 'data-name'}).find('a').text
        parts = date.split(" ")
        date = "".join(parts[:2])

        # Save the collected url in the variable "collected_url"
        collected_url = 'https://data.ibb.gov.tr' + url

        # Save the page that the url
        if collected_url not in downloaded_url_list:
            print("\t", collected_url, flush=True)
            save_link(collected_url, date)


# Call the write_urls_to_file function to write URLs to a text file:
download_links_from_index()
