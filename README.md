# Data Science Project

# Project Description

- Data can be found in (only Sabanci members): https://drive.google.com/drive/folders/19vEpdlu2n6b17rJccsgeiR18Q2d0FyGc?usp=sharing

This project consists of several Python files that perform different tasks related to data processing and analysis. Each file focuses on a specific task and creates specific output files. Here is a brief overview of each Python file and its purpose:

## PY FILE NUMBER 1 (download_ibb_links.py)

This Python algorithm requests data from IBB traffic to obtain download links for each month and year. The downloaded links are saved in the file `ibb_links.txt`.

Creates:
- `ibb_links.txt`: Contains download links for IBB traffic data.

## PY FILE NUMBER 2 (download_ibb_data.py)

This Python algorithm downloads the data from the text file `ibb_links.txt` and saves it in the "MonthYear" format for each month and year. The downloaded data is stored in the directory `ibb_data/` with subdirectories for each month and year.

Creates:
- `ibb_data/`: Directory containing subdirectories for each month and year, e.g., `Ocak2020`, `Nisan2023`.

## PY FILE NUMBER 3 (download_map_links.py)

This Python algorithm creates new CSV files for each MonthYear CSV file by adding Google links for their respective locations. It removes certain columns such as LATITUDE, LONGITUDE, GEOHASH, MINIMUM_SPEED, and MAXIMUM_SPEED. Unique links are saved in the file `map_abbrev.csv` with a rank number appended. All links are saved in the file `map_links.txt`.

Creates:
- `ibb_data_with_MapLink/`: Directory containing CSV files for each MonthYear with added Google links, e.g., `Ocak2020_WmapLink.csv`, `Nisan2023_WmapLink.csv`.
- `map_abbrev.csv`: CSV file containing unique links with rank numbers.
- `map_links.txt`: Text file containing all links.

## PY FILE NUMBER 4 (download_map_html.py)

This Python algorithm converts all Google Map links to DISTRICT by checking each link. To reduce processing time, it saves unique links to a separate CSV file named `mapMATCH_abbrev.csv`. This file can be checked with another Python algorithm. The algorithm takes around 13 hours to process, with approximately 9 seconds for each Google link.

Creates:
- `mapMATCH_abbrev.csv`: CSV file containing unique links with city names added.


## PY FILE NUMBER 5 (match_map_url.py)

This Python algorithm creates new CSV files for each MonthYear CSV file by matching the links added in PY FILE NUMBER 3 with their DISTRICT values. The DISTRICT values are specific to ISTANBUL. The output files are saved in the directory `ibb_data_matched/`.

Creates:
- `ibb_data_matched/`: Directory containing CSV files for each MonthYear with matched links, e.g., `Ocak2020_match.csv`, `Aralik2022_match.csv`.

## PY FILE NUMBER 6 (match_bycity.py)

This Python algorithm creates new CSV files for DISTRICT values by checking every MonthYear CSV file. The algorithm separates DISTRICT values and excludes "Adalar". The output files are saved in the directory `ibb_data_bycity/`.

Creates:
- `ibb_data_bycity/`: Directory containing CSV files for each DISTRICT, e.g., `Avcilar.csv`, `Tuzla.csv`.

## PY FILE NUMBER 7 (set_date_byDay.py)

This Python algorithm creates new CSV files from DISTRICT CSV files. It removes the 'DISTRICT' column, splits the date into pieces, adds missing values into a text file, and sets a new average value for each day. The output files are saved in the directory `ibb_data_byDay/`, and a report is generated in the file `report_ibb_traffic_data.txt`.

Creates:
- `ibb_data_byDay/`: Directory containing CSV files for each DISTRICT with data organized by day, e.g., `Adalar_day.csv`, `Tuzla_day.csv`.
- `report_ibb_traffic_data.txt`: Report file documenting the data processing.

## PY FILE NUMBER 8 (petrol_prices_download.py)

This Python algorithm pulls data of Motorin and Diesel prices from the EPDK website in a bi-monthly period and saves it in Excel (XLS) format. The prices are separated by the Anatolian side (Anadolu) and the European side (Avrupa), stored in different directories.

Creates:
- `petrol_prices_nonorganized/ANADOLU/`: Directory containing Excel files for Diesel and Gasoline prices on the Anatolian side, e.g., `01.01.2020_01.03.2020_ANADOLU_DIESEL.xls`, `01.01.2020_01.03.2020_ANADOLU_GASOLINE.xls`.
- `petrol_prices_nonorganized/AVRUPA/`: Directory containing Excel files for Diesel and Gasoline prices on the European side, e.g., `01.01.2020_01.03.2020_AVRUPA_DIESEL.xls`, `01.01.2020_01.03.2020_AVRUPA_GASOLINE.xls`.

## PY FILE NUMBER 9 (price_organizer.py)

This Python algorithm reads the CSV files extracted by PY FILE NUMBER 8 (petrol_prices_download) and combines all "Europe" and "Anatolian" prices, considering Gasoline and Diesel prices, into two CSV files. The prices are presented in Turkish Lira (TRY) and are organized from 2020-01-01 to 2023-01-01. Missing values are filled with the average value of their respective fuel type.

Creates:
- `petrol_prices/AVRUPA.csv`: CSV file containing the combined European prices for Gasoline and Diesel.
- `petrol_prices/ANADOLU.csv`: CSV file containing the combined Anatolian prices for Gasoline and Diesel.


## Known Problems

While working on the project, the following problems have been identified:

### PY FILE NUMBER 1 (download_ibb_links.py)
- No known problems.

### PY FILE NUMBER 2 (download_ibb_data.py)
- No known problems.

### PY FILE NUMBER 3 (download_map_links.py)
- Some latitude and longitude values may be written in the opposite order.

### PY FILE NUMBER 4 (download_map_html.py)
- The processing time is approximately 13 hours, with around 9 seconds for each Google link.

### PY FILE NUMBER 5 (match_map_url.py)
- Some link indexes may be shifted, resulting in missing data for "Haziran2021".
- The values from 2023 may not match correctly, so only data from two years is considered.

### PY FILE NUMBER 6 (match_bycity.py)
- No known problems.

### PY FILE NUMBER 7 (set_date_byDay.py)
- No known problems.

### PY FILE NUMBER 8 (petrol_prices_download.py)
- The website only allows searching data in a 3-month period, so the algorithm pulls data in a 2-month period instead.

### PY FILE NUMBER 9 (price_organizer.py)
- There were some missing values in the data, which were filled with the average value of their kind (Gasoline or Diesel).


## Requirements

The following packages and libraries are required to run the Python scripts:

- os
- sys
- glob
- re
- requests
- BeautifulSoup from bs4
- json
- pprint from pprint
- pandas as pd
- numpy as np
- uuid
- csv
- webdriver from selenium
- chrome.service from selenium.webdriver.chrome.service
- Keys from selenium.webdriver.common.keys
- BeautifulSoup from bs4
- Select from selenium.webdriver.support.ui
- By from selenium.webdriver.common.by
- time
- datetime from datetime
- relativedelta from dateutil.relativedelta
- timedelta from datetime
- webdriver from selenium
- ChromeDriver (web driver for Selenium)

It is assumed that the required ChromeDriver executable file is already installed and configured properly. Make sure to install any missing packages using pip or your preferred package manager before running the scripts.
