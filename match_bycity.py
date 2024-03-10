'''
# PY FILE NUMBER 6

This python algorithm will be creating new csv files for DISTRICT values.
It will check every MonthYear.csv files and seperate DISTRICT values
> Also, Adalar is removed, and not included

Creates: ibb_data_bycity/
                         Avcilar.csv
                         ...
                         Tuzla.csv

Problem:

'''

import pandas as pd
import os
import csv
import re

ENCODINGS = "utf-8"

months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

DIREC_PATH = 'ibb_data_bycity'

DATA_DIR = 'ibb_data_matched/'

ist = ['Avcılar', 'Arnavutköy', 'Ataşehir', 'Bağcılar',
       'Bahçelievler', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beşiktaş',
       'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca',
       'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüpsultan', 'Fatih',
       'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kâğıthane', 'Kartal',
       'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe', 'Sarıyer',
       'Silivri', 'Sultanbeyli', 'Sultangazi', 'Şile', 'Şişli', 'Tuzla',
       'Ümraniye', 'Üsküdar', 'Zeytinburnu']

if not os.path.exists(DIREC_PATH):
    os.makedirs(DIREC_PATH)


for city in ist:
    output_file = DIREC_PATH + '/' + city

    # Create temp dataframe
    temp_df_columns = ['DISTRICT', 'DATE_TIME', 'AVERAGE_SPEED', 'NUMBER_OF_VEHICLES']
    temp_df = pd.DataFrame(columns=temp_df_columns)
    # Create lists to add dataframe later
    districts = []
    date_time = []
    average_speed = []
    num_vehicles = []
    # Check every MonthYear.csv file
    for j in range(2020, 2023):
        for i in months:
            input_filename = DATA_DIR + i + str(j) + '_match.csv'
            try:
                with open(input_filename, 'r', encoding= ENCODINGS) as f:
                    reader = csv.reader(f)

                    for row in reader:
                        # Check every row and format district value
                        district = row[1]
                        matches = re.findall(r'\w+', district)

                        # If city matches, add to the list
                        if matches[0] == city:
                            print(city)
                            districts.append(row[1])
                            date_time.append(row[2])
                            average_speed.append(row[3])
                            num_vehicles.append(row[4])
            except FileNotFoundError:
                print("File not found error:", input_filename)
                # Haziran2021.csv file has a problem
                continue
    # Finish by adding to data frame
    temp_df['DISTRICT'] = districts
    temp_df['DATE_TIME'] = date_time
    temp_df['AVERAGE_SPEED'] = average_speed
    temp_df['NUMBER_OF_VEHICLES'] = num_vehicles

    # Save it as a csv file named DISTRICT
    temp_df.to_csv(output_file, index=False)
