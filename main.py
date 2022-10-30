
import csv
import datetime
import pandas as pd
lists = [[] for i in range(7)]

with open(r"C:\Users\HP\Downloads\GD1.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        for i in range(0, len(row)): lists[i].append(row[i])

for i in range(1, 7):
    lists[i] = [float(j) for j in lists[i]]

lists[0] = [datetime.datetime.strptime(j, "%Y-%m-%d") for j in lists[0]]

diction = {'Date': lists[0], 'Open': lists[1], 'High': lists[2],
           'Low': lists[3], 'Close': lists[4], 'Adj close': lists[5], 'Volume': lists[6]}
df = pd.DataFrame(diction)
df.columns = ['New Date', 'New Open', 'New High', 'New Low', 'New Close', 'New Adj Close', 'New Volume']

lists.append([])
lists.append([])
lists.append([])
for i in range(len(lists[0])):
    lists[7].append('Amangeldy')
    lists[8].append('Rakhimzhanov')
    lists[9].append(datetime.datetime.strptime('2022-09-14', "%Y-%m-%d"))
df.insert(7,"Name", lists[7])
df.insert(8,"Surname", lists[8])
df.insert(9,"Date_of_download", lists[9])
# print(df.iloc[range(0, 10), range(0, 10)])
# print(df.head(10))
# print(df.iloc[range(len(lists[0])-10, len(lists[0])), range(0, 10)])
# print(df.tail(10))

# # df.to_json(r'C:\Users\User\Desktop\КБТУ\ICT(2course)\Practice2.json')


data_begin = datetime.datetime(year=2021, month = 6, day = 1)
data_end = datetime.datetime(year=2021, month = 9, day = 1)
print(df[(df['New Date'] > data_begin) & (df['New Date'] < data_end)])

# data_begin = datetime.datetime(year=2021, month = 1, day = 1)
# data_end = datetime.datetime(year=2021, month = 3, day = 1)

# df = df[(df['New Date'] > data_begin) & (df['New Date'] < data_end)]
# print(df)
# average = df['New Volume'].mean()
# print(df[df['New Volume'] > average].loc[:, ['New Open', 'New Close', 'New High']])



