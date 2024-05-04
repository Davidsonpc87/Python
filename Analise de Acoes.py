from tkinter.tix import DisplayStyle
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

cotacao_bovespa = web.DataReader('^BVSP', data_source = 'yahoo', start= "01-02-2020", end= "01-01-2021")
DisplayStyle(cotacao_bovespa)

