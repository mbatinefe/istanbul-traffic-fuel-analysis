'''
# PY FILE NUMBER 2

This python algorithm will be downloading the data from the text file called ibb_links.txt
That downloaded data will be saved as MonthYear format for each month and each year.

Creates: ibb_data/
                  Ocak2020
                  ...
                  Nisan2023
Problem: NaN
'''

import os, sys, glob, re
import requests
from bs4 import BeautifulSoup as bs

LINK_LIST_PATH = 'ibb_links.txt'
DATA_DIR = 'ibb_data/'

# Encoding for writing the page html files
ENCODING = "utf-8"

direc_path = "ibb_data"
if not os.path.exists(direc_path):
    os.makedirs(direc_path)

def save_html_pages():
    with open(LINK_LIST_PATH, "r", encoding=ENCODING) as file:
        first_line_skipped = False  # Flag variable to skip the first line
        for line in file:
            if not first_line_skipped:
                first_line_skipped = True
                continue  # Skip the first iteration
            # Process each line here
            line = line.strip()  # Remove whitespaces

            # Split the line by tab to separate the URL and date
            url, filename = line.split("\t")

            # Create the save directory if it doesn't exist
            os.makedirs(DATA_DIR, exist_ok=True)

            # Build the complete path to save the file
            save_path = os.path.join(DATA_DIR, filename + '.csv')

            # Send a GET request to download the file
            resp = requests.get(url)
            soup = bs(resp.content, 'html.parser')
            link = soup.find('div', {'role': 'main'}).find('div', {'class': 'actions'}).find('a')['href']
            response = requests.get(link)

            # Check if the request was successful
            if response.status_code == 200:
                with open(save_path, "wb") as file2:
                    file2.write(response.content)
                print("File downloaded successfully.")
            else:
                print("Failed to download the file.")


save_html_pages()
