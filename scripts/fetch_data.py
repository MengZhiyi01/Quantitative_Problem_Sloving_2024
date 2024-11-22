## This is just a test
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta
import os

# Define the start and end dates for the last 4 quarters
end_date = datetime.now()
start_date = end_date - timedelta(days=365*4)

# Fetch the CPI data from the Federal Reserve Bank of St. Louis (FRED)
cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)

# Calculate the inflation rate for the last 4 quarters
# Assuming the CPI data is monthly, we'll calculate the quarterly change
quarters = cpi_data.resample('QE').last()

# Calculate the percentage change from one quarter to the next
inflation_rates = quarters.pct_change() * 100

# Print the last 4 quarters of inflation
print(inflation_rates.tail(4))

# Create the 'data' directory if it does not exist
data_dir = '../data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Save the inflation rates to a CSV file
inflation_rates.to_csv(f'{data_dir}/inflation_rates.csv')