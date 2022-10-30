import csv
import datetime
import pandas as pd
df = pd.read_csv(r"C:\Users\HP\Downloads\pythgg\GD1.csv", parse_dates = ["Date"])
print(type(df['Date'][0]))
df['Name'] = 'Aman' 
df['Surname'] = 'Rakhimzhanov'
df['Date_of_download'] = datetime.datetime.strptime('2022-09-07', "%Y-%m-%d")
df['Percentage_change'] = [for ё]
print(df)