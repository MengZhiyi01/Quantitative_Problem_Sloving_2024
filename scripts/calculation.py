## This is just a test
import pandas as pd
import pandas_datareader.data as web
from src.utils import *
import os

# Use the function in src.utils
cpi_data = fetch_data_and_clean('CPIAUCSL', 'fred', start_date = '2015-01-01')

# Calculate the inflation rate for the last 4 quarters
quarters = cpi_data.resample('QE').mean()
inflation_rates = quarters.pct_change() * 100
inflation_rates.dropna(inplace=True)

# Print the last 4 quarters of inflation
print(f'The last 4 quarters of inflation are:\n{inflation_rates.tail(4)}')

# Create the 'data' directory if it does not exist
data_dir = '../data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Save the inflation rates to a CSV file
inflation_rates.to_csv(f'{data_dir}/inflation_rates.csv')