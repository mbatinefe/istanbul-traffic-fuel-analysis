'''
# PY FILE NUMBER 4
We needed to convert all google map links to DISTRICT by checking each of
    them. However, there were millions of links that needed to be checked.
    We thought that saving unique links to another csv file will be decreasing
    the amount of time for going through every link. That unique
    csv file can be checked with another python algorithm. We succeeded to
    decrease to only 5014 links.

Then, python algorithm will be creating new csv file from map_abbrev.csv.
    > By adding city name to link IDs

Creates: mapMATCH_abbrev.csv

Problem:
    # Processing took around 13 hours.
        > Around 9 seconds for each google link

'''

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

ENCODING = "utf-8"

SAVE_PATH_CITY = 'mapMATCH_abbrev.csv'

ist = ['Adalar', 'Arnavutköy', 'Ataşehir', 'Avcılar', 'Bağcılar',
       'Bahçelievler', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beşiktaş',
       'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca',
       'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüpsultan', 'Fatih',
       'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kâğıthane', 'Kartal',
       'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe', 'Sarıyer',
       'Silivri', 'Sultanbeyli', 'Sultangazi', 'Şile', 'Şişli', 'Tuzla',
       'Ümraniye', 'Üsküdar', 'Zeytinburnu']

df = pd.DataFrame(columns=['ID', 'CITY', 'URL'])

downloaded_links = []

EXECUTABLE_PATH = 'C:/Users/mbefe/OneDrive/Desktop/chromedriver_win32/chromedriver.exe'

NUMBER_list = []
CITY_list = []
URL_list = []

count_a = 1

with open('map_abbrev.csv', 'r', encoding=ENCODING) as file:
    # Open the output CSV file
    reader = csv.reader(file)

    for line in reader:
        if line != ['0']:

            # To see the process
            print(count_a)
            count_a = count_a + 1

            # Split the line using the "@" delimiter
            elements = line[0].split('@')

            # Retrieve the first element (URL)
            url = elements[0]

            # Remove "" occurences of the links
            url = re.sub('"{2,}', '"', url)

            # Configure the Selenium webdriver with Chrome
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # Run Chrome in headless mode

            # Create a Service object with the path to the Chrome web driver
            SERVICE = Service(executable_path=EXECUTABLE_PATH)

            # Start the service
            SERVICE.start()

            # Pass the Service object to the webdriver
            driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)

            # Load the webpage
            driver.get(url)

            # Get the current page's HTML content
            html_content = driver.page_source

            # Create a BeautifulSoup object to parse the HTML
            soup = bs(html_content, 'html.parser')

            if soup.find('div', {'data-section-id': '334'}) is not None:
                temp = soup.find('div', {'data-section-id': '334'})
                if temp.find('span', {'class': 'DkEaL'}) is not None:
                    location = temp.find('span', {'class': 'DkEaL'}).text
                else:
                    location = "NONE"
            else:
                location = "NONE"

            print(location)

            # Close the browser and the service
            driver.quit()
            SERVICE.stop()

            ####
            # Compile a pattern to match any of the districts from the ist list
            pattern = re.compile(r'\b(?:{})\b'.format('|'.join(ist)), re.IGNORECASE)

            # Find all matches of the pattern in the given text
            matches = re.findall(pattern, location)

            # Add to list for adding df to write on csv
            NUMBER_list.append(elements[1])
            URL_list.append(url)

            if matches:
                print("Match found. District(s):", ', '.join(matches))
                CITY_list.append(matches)
            else:
                CITY_list.append("DNE")
                print("No matches found.")

df['ID'] = NUMBER_list
df['CITY'] = CITY_list
df['URL'] = URL_list
# Save the DataFrame to a CSV file
df.to_csv(SAVE_PATH_CITY, index=False)
