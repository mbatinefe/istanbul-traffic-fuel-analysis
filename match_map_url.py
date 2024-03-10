'''
# PY FILE NUMBER 5

This python algorithm will be creating new csv files for MonthYear csv files.
    > By matching all the links we added in PY FILE NUMBER 3 with it is DISTRICT value
        > DISTRICT values of ISTANBUL

All links will be saved as map_links.txt

Creates: ibb_data_matched/
                              Ocak2020_match.csv
                              ...
                              Aralik2022_match.csv

Problem:
    # Some of links indexes are shifted, that is why we lost "Haziran2021"
    # We were going to take it however, it would be WRONG DATA, and might cause
      in serious skew while creating tables.
    # Values from 2023 also mismatched that is why we decided to continue with two years' value.

'''

import csv
import pandas as pd
import os

ENCODING = "utf-8"
BASE_ABBREV = 'mapMATCH_abbrev.csv'
months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

DIREC_PATH = 'ibb_data_matched'

DATA_DIR = 'ibb_data_with_MapLink/'

# Create a list to add to df later
ID_list = []
CITY_list = []
DATE_list = []
AVER_list = []
VEHIC_list = []
URL_list = []

process_count = 0

# To store the values in DISTRICT - ID
temp_id = []
temp_city = []
with open(BASE_ABBREV, 'r', encoding=ENCODING) as file:
    # Open the output CSV file
    reader = csv.reader(file)
    if not os.path.exists(DIREC_PATH):
        os.makedirs(DIREC_PATH)

    for row in reader:
        temp_id.append(row[0])
        temp_city.append(row[1])

for j in range(2020, 2023):
    for i in months:
        filename = DATA_DIR + i + str(j) +'_WmapLink.csv'
        try:
            print(i, j)
            print(process_count)
            process_count = process_count + 1

            df = pd.read_csv(filename)
            new_df_columns = ['ID', 'DISTRICT', 'DATE_TIME', 'AVERAGE_SPEED', 'NUMBER_OF_VEHICLES', 'LOCATION_LINKS']
            new_df = pd.DataFrame(columns=new_df_columns)

            # Copy other dataframes to newDF that we will not touch
            new_df['ID'] = df['LOCATION_NUM']
            new_df['LOCATION_LINKS'] = df['LOCATION_LINKS']
            new_df['DATE_TIME'] = df['DATE_TIME']
            new_df['AVERAGE_SPEED'] = df['AVERAGE_SPEED']
            new_df['NUMBER_OF_VEHICLES'] = df['NUMBER_OF_VEHICLES']

            # Set file direct
            direc_file = 'ibb_data_matched/' + i + str(j) + '_match.csv'
            count = 0

            temp_df = []
            # Iterate through each row and if we find the id in LOCATION NUM of MonthDate.csv files,
            # Add it to the temp_df to add as a DISTRICT value in the end.
            for index, row in df.iterrows():
                id_match = row['LOCATION_NUM']
                search = id_match
                try:
                    indices = temp_id.index(str(search))
                    temp_df.append(temp_city[int(indices)+1])
                except ValueError:
                    # if 0 - Basaksehir, https://www.google.com/maps/place/41°4'50.3""N+28°48'41.9""E
                    temp_df.append(['Başakşehir'])
                    continue

            new_df['DISTRICT'] = temp_df
            # Create as a new file
            new_df.to_csv(direc_file, index=False)
        except Exception as e:
            print(f"An error occurred: {str(e)}", filename)
            continue

