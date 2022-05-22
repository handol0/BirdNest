import pandas_datareader
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

writer = pd.ExcelWriter('E:\Folder\data\charlie.xlsx')

Ticker =  ['BA', 'TSLA', 'NKE', '^DJI']

dataBTND = pdr.get_data_yahoo(Ticker, start="2012-01-01", end="2021-12-31", interval='m')
dataBTND = dataBTND['Close']

dataBTND.to_excel(writer, sheet_name='Sheet1', header=True)

#================================================================================

Ticker2 = ['GC=F','^IRX']
dataGI = pdr.get_data_yahoo(Ticker2, start="2012-01-01", end="2021-12-31", interval='m')
dataGI = dataGI['Close']

dataGI.to_excel(writer, sheet_name='Sheet2', header=True)
<<<<<<< HEAD
writer.save()
=======
writer.save()




# Checking Push Request
>>>>>>> 9e34a6ba6a3d9caefaea4265e339b8ceacc4514e
