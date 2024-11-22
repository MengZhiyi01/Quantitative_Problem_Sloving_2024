## This is just a test
import os
import sys
from datetime import datetime, timedelta

import pandas_datareader.data as web
import pandas as pd

# Add src directory to the system path for importing utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src.utils import calculate_quarterly_inflation

def fetch_cpi_data():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * 2)
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start_date, end_date)
    return cpi_data

def main():
    # Fetch CPI data
    cpi_data = fetch_cpi_data()

    # Calculate quarterly inflation
    quarterly_inflation = calculate_quarterly_inflation(cpi_data)

    # Report the last four quarters of inflation
    last_four_quarters = quarterly_inflation.tail(4)
    print("Last 4 Quarters of US Inflation (in percentage):")
    print(last_four_quarters)

if __name__ == "__main__":
    main()
