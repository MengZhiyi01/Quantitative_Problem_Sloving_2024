## This is just a test
import pandas as pd

def calculate_quarterly_inflation(cpi_data):
    cpi_data['Quarter'] = cpi_data.index.to_period('Q')
    quarterly_cpi = cpi_data.resample('Q').mean()
    quarterly_inflation = quarterly_cpi.pct_change().dropna() * 100
    return quarterly_inflation
