'''
# PY FILE NUMBER 9

This python algorithm will be reading the csv files extracted from previous from petrol_prices_download. The code
will combine all "Europe" and "Anatolian" prices with considering Gasoline and Diesel prices in a two csv file. 

Prices in TRY (Turkish Lira)

It will check every csv files and
> Add date column and order starting from 2020-01-01 to 2023-01-01
> Fill missing values with average of its fuel kind
> AVRUPA.csv/
    #     DATE          GASOLINE_PRICE     DIESEL_PRICE
    >    2020-01-01         6.99               6.51
    >    2020-01-02         7.00               6.52
            .....
    >    2022-12-31         19.45              22.02    
    >    2023-01-01         19.51              22.08    

> ANADOLU.csv/
    #     DATE          GASOLINE_PRICE     DIESEL_PRICE
    >    2020-01-01         7.05               6.54
    >    2020-01-02         7.06               6.55
            .....
    >    2022-12-31         19.46              22.03    
    >    2023-01-01         19.48              22.05    
   
Creates: petrol_prices/
                      AVRUPA.csv # European side
                      ANADOLU.csv # Anatolian side

Problem:
    > There was some missing values, and filled with average of its kind (Gasoline or Diesel)

'''
from datetime import datetime, timedelta
import pandas as pd
import os
import numpy as np

# Set the main and output directories
MAIN_DIRECTORY = 'petrol_prices_nonorganized'
OUT_DIRECTORY = 'petrol_prices'

for directory in os.listdir(MAIN_DIRECTORY):
    # Create an empty dataframe with columns "DATE" "GASOLINE_PRICE" "DIESEL_PRICE"
    temp_df_columns = ['DATE', 'GASOLINE_PRICE', 'DIESEL_PRICE']
    temp_df = pd.DataFrame(columns=temp_df_columns)

    start_date = datetime.strptime("01.01.2020", "%d.%m.%Y")
    end_date = datetime.strptime("01.01.2023", "%d.%m.%Y")

    current_date = start_date
    # Add the temporary dataframe with dates from start_date to end_date
    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        temp_df.loc[len(temp_df)] = [formatted_date, np.nan, np.nan]
        current_date += timedelta(days=1)

    for filename in os.listdir(os.path.join(MAIN_DIRECTORY, directory)):
        file_path = os.path.join(MAIN_DIRECTORY, directory, filename)
        # Read the Excel file to DataFrame
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            real_index = (datetime.strptime(df.loc[index, 'Tarih'], "%d.%m.%Y") - start_date).days
            # Fill appropriate column in the temporary dataframe considering the fuel type
            if df.loc[index, 'Yakıt Tipi'] == 'Motorin':
                temp_df.loc[real_index, 'DIESEL_PRICE'] = df.loc[index, 'Fiyat']
            else:
                temp_df.loc[real_index, 'GASOLINE_PRICE'] = df.loc[index, 'Fiyat']

    # Fill missing values in the temporary dataframe
    temp_df['DIESEL_PRICE'].fillna(method='bfill', inplace=True, limit=1)
    temp_df['DIESEL_PRICE'].fillna(method='ffill', inplace=True)
    temp_df['GASOLINE_PRICE'].fillna(method='bfill', inplace=True, limit=1)
    temp_df['GASOLINE_PRICE'].fillna(method='ffill', inplace=True)

    output_file = OUT_DIRECTORY + '\\' + directory + '.csv'
    # Save the temporary dataframe to a CSV file
    temp_df.to_csv(output_file, index=False)