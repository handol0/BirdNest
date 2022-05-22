import pandas_datareader
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

writer = pd.ExcelWriter('E:\Folder\data\charlie.xlsx')


dataBA = pdr.get_data_yahoo("BA", start="2012-01-01", end="2021-12-31", interval='m')
dataBA = dataBA['Close']
#dataBA['CName'] = "The Boeing Company"

dataTesla = pdr.get_data_yahoo("TSLA", start="2012-01-01", end="2021-12-31", interval='m')
dataTesla = dataTesla['Close']
#dataTesla['CName'] = "TESLA"

dataNike = pdr.get_data_yahoo("NKE", start="2012-01-01", end="2021-12-31", interval='m')
dataNike = dataNike['Close']
#dataNike['CName'] = "Nike, Inc"

dataDJ = pdr.get_data_yahoo("^DJI", start="2012-01-01", end="2021-12-31", interval='m')
dataDJ = dataDJ['Close']
#dataDJ['CName'] = "Dow Jones"
print(dataBA)


#union진행 필요
union_all=pd.concat([dataBA, dataTesla, dataNike, dataDJ])



union_all.to_excel(writer, sheet_name='KOSPI', header=True)
writer.save()


#checking branches