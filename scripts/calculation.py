## This is just a test
import pandas as pd
from src.utils import *
import os

# Use the function in src.utils
def generate_inflation(name = 'CPIAUCSL', source = 'fred', end_date = datetime.now(), start_date = datetime.now() - timedelta(days=365*4), save = True):
    cpi_data = fetch_data_and_clean('CPIAUCSL', 'fred', start_date = '2015-01-01')

    # Calculate the inflation rate for the last 4 quarters
    quarters = cpi_data.resample('QE').mean()
    inflation_rates = quarters.pct_change() * 100

    # Rename the columns
    inflation_rates.rename(columns={'CPIAUCSL': 'Inflation_rate'},inplace=True)
    inflation_rates.dropna(inplace=True)

    # Convert the date format to quarters
    inflation_rates['Date'] = inflation_rates.index.to_period('Q')
    inflation_rates.reset_index(inplace=True)
    inflation_rates = inflation_rates[['Date', 'Inflation_rate']]

    # Create the 'data' directory if it does not exist
    if save:
        data_dir = '../data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Save the inflation rates to a CSV file
        inflation_rates.to_csv(f'{data_dir}/inflation_rates.csv')

    return inflation_rates

if __name__=="__main__":
    # Print the last 4 quarters of inflation
    inflation_rates = generate_inflation()
    print(f'The last 4 quarters of inflation are:\n{inflation_rates.tail(4)}')

    # Print all cpi data
    print(f'The all the inflation rates are:\n{inflation_rates}')