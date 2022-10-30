from  bs4 import BeautifulSoup
import  csv
import pandas as pd
import requests

list0 = []
with open(r'list_symbols_euronext.csv','r') as file:
    csvfile1 = csv.reader(file)
    for row in csvfile1:
        for i in row:
            list0.append(i)

with open(r'list_symbols_US.csv','r') as file:
    csvfile2 = csv.reader(file)
    for row in csvfile2:
        for i in row:
            list0.append(i)
listOfDf = []
for i in range(10):
    url = "https://query1.finance.yahoo.com/v7/finance/download/{}?period1=0&period2=1661904000&interval=1d&events=history&includeAdjustedClose=true".format(list0[i])
    try:
        df = pd.read_csv(url)
        df['name_of_the_company'] = list0[i]
        listOfDf.append(df)
        #print(df)
    except:
        pass

final = pd.concat(listOfDf)
final.to_parquet('df_final_US_EUR.parquet')
final.to_csv('df_final_US_EUR.csv')

dfParquet = pd.read_parquet('df_final_US_EUR.parquet')
print(dfParquet)