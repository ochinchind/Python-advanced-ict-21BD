import pandas as pd
import csv
brand = ['Coca', 'Pepsi', 'Sprite', 'water']
taste = 5, 6, 9, 8
sugar_content = 'high', 'high', 'high', 'low'

df = pd.DataFrame([brand, taste, sugar_content])

print(df)

a = [1,2,3]
b = ['a', 'b', 'c']
zipped_list = list(zip(a,b))
print(zipped_list)

zipped_list = list(zip(brand,taste))
print(zipped_list)

df = pd.read_csv(r"C:\Users\HP\Downloads\pythgg\Apple.csv", parse_dates = "Date")
print(df)

print(type(df['Date'][0]))


df= df.sort_values('Open_price')
print(df)