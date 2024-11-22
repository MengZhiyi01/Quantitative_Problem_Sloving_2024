## This is just a test

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta

def fetch_data_and_clean(name = 'CPIAUCSL', source = 'fred', end_date = datetime.now(), start_date = datetime.now() - timedelta(days=365*4)):
    '''
    Fetch the CPI data from the Federal Reserve Bank of St. Louis (FRED)
    :param name: defualt: CPIAUCSL
    :param source: defualt: FRED
    :param end_date: defualt: now
    :param start_date: defualt: 4 years ago
    :return: dataframe with Nan ovservation dropped
    '''
    data = web.DataReader(name = name,
                          data_source = source,
                          start = start_date,
                          end = end_date)

    data.dropna(inplace=True)

    return data
