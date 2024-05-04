from alpha_vantage.timeseries import TimeSeries
ts =  TimeSeries(key = 'FKNTJFNGUERJ7987', output_format = 'pandas')

MSFT_av, metadata = ts.get_daily_adjusted ('MSFT', outputsize= 'full')
MSFT_av        

import pandas as pd
from pandas_datareader import data as wb



df = wb.DataReader('MSFT', data_source='yahoo', start='1-1-2015')
df.tail()