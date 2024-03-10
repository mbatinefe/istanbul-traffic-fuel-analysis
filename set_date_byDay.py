'''
# PY FILE NUMBER 7

This python algorithm will be creating new csv files from DISTRICT csv files.

It will check every DISTRICT.csv files and
> Remove 'DISTRICT' Column
> Split Date into pieces
> Add missing values into txt file
> Set new average value for day
    > 2020-08-01 00:00:00   CAR_NUM_1   AV_SPEED_1
    > 2020-08-01 01:00:00   CAR_NUM_2   AV_SPEED_2
    ...
    > 2020-08-01 23:00:00   CAR_NUM_24   AV_SPEED_24

    =======
                        (CAR_NUM_1 x AV_SPEED_1) + .... + (CAR_NUM_N x AV_SPEED_N)
      > new_av_daily = -----------------------------------------------------------
                         (CAR_NUM_1 + .... + CAR_NUM_N)
Creates: ibb_data_byDay/
                         Adalar_day.csv
                         ...
                         Tuzla_day.csv

         report_ibb_traffic_data.txt

Problem:

'''
import pandas as pd
import os
import csv
from datetime import datetime, timedelta

ENCODINGS = 'utf-8'
DIREC_PATH = 'ibb_data_byDay'
DATA_DIR = 'ibb_data_bycity'
REPORT_FILE_PATH = 'report_ibb_traffic_data.txt'

# List of districts
ist = ['Avcılar', 'Arnavutköy', 'Ataşehir', 'Bağcılar',
       'Bahçelievler', 'Bakırköy', 'Başakşehir', 'Bayrampaşa', 'Beşiktaş',
       'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca',
       'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüpsultan', 'Fatih',
       'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kâğıthane', 'Kartal',
       'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe', 'Sarıyer',
       'Silivri', 'Sultanbeyli', 'Sultangazi', 'Şile', 'Şişli', 'Tuzla',
       'Ümraniye', 'Üsküdar', 'Zeytinburnu']

# Create base path if it doesn't exist for new csv files
if not os.path.exists(DIREC_PATH):
    os.makedirs(DIREC_PATH)

# Loop through each district
for city in ist:
    input_file = DATA_DIR + '\\' + city + '.csv'
    output_file = DIREC_PATH + '\\' + city + '.csv'

    print(city)

    # Create temp dataframe
    temp_df_columns = ['DATE', 'AVERAGE', 'CAR']
    temp_df = pd.DataFrame(columns=temp_df_columns)

    # Define start and end dates
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2022-12-31", "%Y-%m-%d")

    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        temp_df.loc[len(temp_df)] = [formatted_date, 0.0, 0.0]
        current_date += timedelta(days=1)


    try:
        # Read the input file
        with open(input_file, 'r', encoding=ENCODINGS) as f:
            reader = csv.DictReader(f)
            for row in reader:
                date_time = row['DATE_TIME'][0:10]
                average_speed = float(row['AVERAGE_SPEED'])
                num_vehicles = float(row['NUMBER_OF_VEHICLES'])
                # Calculate index based on the date
                index = (datetime.strptime(date_time, "%Y-%m-%d") - start_date).days
                x = average_speed * num_vehicles
                temp_df.loc[index, 'AVERAGE'] += x
                temp_df.loc[index, 'CAR'] += num_vehicles

    except FileNotFoundError:
        print("File not found error:", input_file)

    # Calculate new average values
    temp_df['RESULT'] = temp_df['AVERAGE'] / temp_df['CAR']
    temp_df.drop(['AVERAGE', 'CAR'], axis=1, inplace=True)

    # Handle missing values
    missing_values_count = temp_df['RESULT'].isnull().sum()
    temp_df['RESULT'].fillna(temp_df['RESULT'].mean(), inplace=True)

    # Write report to file for missings
    report = f"{missing_values_count} missing days filled with average value in file {city}.csv"
    with open(REPORT_FILE_PATH, 'a+', encoding='utf-8') as file:
        file.write(report + '\n')

    # Save it as a csv file named DISTRICT.csv
    temp_df.to_csv(output_file, index=False)