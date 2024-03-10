'''
# PY FILE NUMBER 3

This python algorithm will be creating new csv files for MonthYear csv files.
    > By adding google links for its location
    > By removing LATITUDE, LONGITUDE, GEOHASH, MINIMUM_SPEED, MAXIMUM_SPEED.

Unique links will be saved as map_abbrev.csv with its rank number in the end.
    > Further explanation is on FILE NUMBER 4

All links will be saved as map_links.txt

Creates: ibb_data_with_MapLink/
                              Ocak2020_WmapLink.csv
                              ...
                              Nisan2023_WmapLink.csv
         map_abbrev.csv
         map_links.txt
Problem:
    # Some Lattitude and Longitude values are written as opposite
    # Processing took around 5 hours
'''

import pandas as pd
import os

DATA_DIR = 'ibb_data/'
ENCODING = "utf-8"
SAVE_PATH = 'map_links.txt'
SAVE_PATH_2 = 'map_abbrev.csv'
count = 0
count_2 = 0
months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

direc_path = "ibb_data_with_MapLink"

unique_map = []
unique_map_raw = []


if not os.path.exists(direc_path):
    os.makedirs(direc_path)

for j in range(2020, 2023):
    for i in months:
        filename = DATA_DIR + i + str(j) + '.csv'
        new_column_LONG_LAT_link = []
        # Open the CVS file
        try:
            df = pd.read_csv(filename)
            new_df_columns = ['LOCATION_NUM', 'DATE_TIME', 'AVERAGE_SPEED', 'NUMBER_OF_VEHICLES', 'LOCATION_LINKS']
            new_df = pd.DataFrame(columns=new_df_columns)
            # Copy df values to new_df
            new_df['DATE_TIME'] = df['DATE_TIME']
            new_df['AVERAGE_SPEED'] = df['AVERAGE_SPEED']
            new_df['NUMBER_OF_VEHICLES'] = df['NUMBER_OF_VEHICLES']

            # Set file direct
            direc_file = 'ibb_data_with_MapLink/' + i + str(j) + '_WmapLink'
            abbrev_map = []
            for index, row in df.iterrows():
                # Access the values in each column of the current row
                latitude_value = row['LATITUDE']
                longitude_value = row['LONGITUDE']
                date_value = str(row['DATE_TIME'])
                average_speed_value = str(row['AVERAGE_SPEED'])
                vehicles_value = str(row['NUMBER_OF_VEHICLES'])

                # For some of the data, longitude and latitude is written opposite
                # So, we check every latitude and longitude.
                # If taken longitude is lower than 30, it is our needed longitude
                if longitude_value < 30:
                    temp_lat = latitude_value
                    temp_long = longitude_value
                else:
                    temp_lat = longitude_value
                    temp_long = latitude_value

                # Creating coordinates for url extension
                integer_first_lat = int(temp_lat)
                integer_mid_lat_float = (temp_lat - integer_first_lat) * 60
                integer_mid_lat = int(integer_mid_lat_float)
                integer_last_lat_float = (integer_mid_lat_float - integer_mid_lat) * 60
                integer_last_lat = "{:.1f}".format(integer_last_lat_float)

                integer_first_long = int(temp_long)
                integer_mid_long_float = (temp_long - integer_first_long) * 60
                integer_mid_long = int(integer_mid_long_float)
                integer_last_long_float = (integer_mid_long_float - integer_mid_long) * 60
                integer_last_long = "{:.1f}".format(integer_last_long_float)

                url = 'https://www.google.com/maps/place/' + str(integer_first_lat) + '°' \
                      + str(integer_mid_lat) + '\'' + str(integer_last_lat) + "\"N+" \
                      + str(integer_first_long) + '°' + str(integer_mid_long) + '\'' + str(integer_last_long) + "\"E"
                # Make the URL
                print(url, count)
                new_column_LONG_LAT_link.append(url)
                count += 1

                location_value = url

                if location_value not in unique_map_raw:
                    count_2 += 1
                    unique_map.append(location_value + "@" + str(count_2))
                    unique_map_raw.append(location_value)
                    abbrev_map.append(str(count_2))
                    print(count_2)
                else:
                    index = unique_map_raw.index(location_value)
                    abbrev_map.append(str(index))

                # Following code will write all map links on map_links.txt
                if not os.path.exists(SAVE_PATH):
                    with open(SAVE_PATH, "w", encoding=ENCODING) as f:
                        f.write("\t".join(['Google Maps Links']) + "\n")
                        f.write("\t".join([url]) + "\n")

                else:
                    if url in SAVE_PATH:
                        continue
                    else:
                        with open(SAVE_PATH, "a", encoding=ENCODING) as f:
                            f.write("\t".join([url]) + "\n")


            # Add Location Links to new_df and create csv file
            new_df['LOCATION_LINKS'] = new_column_LONG_LAT_link
            new_df['LOCATION_NUM'] = abbrev_map
            new_df.to_csv(direc_file, index=False)

        except Exception as e:
            print(f"An error occurred: {str(e)}", filename)

# Activate if you want to create map_abbrev.csv

df = pd.DataFrame(unique_map)
# Save the DataFrame to a CSV file
df.to_csv(SAVE_PATH_2, index=False)
