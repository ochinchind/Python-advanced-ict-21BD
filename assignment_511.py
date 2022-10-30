'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
import pandas as pd
import csv
import datetime

na_value = ['_', 'error', 'na', '-']
df = pd.read_csv('attendance_to_clean.csv', na_values = na_value)

for index, row in df.iterrows():
    try:
        int(row['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT'] = np.NAN
    except:
        pass

for index, row in df.iterrows():
    try:
        int(row['COUNT'])
    except:
        df.loc[index, 'COUNT'] = np.NAN

for index, row in df.iterrows():
    try:
        datetime.datetime.strptime(row['DATE'], '%Y-%m-%d')
    except:
        df.loc[index, 'DATE'] = np.NAN

df.dropna(inplace=True)

for index, row in df.iterrows():
    if( float(row['COUNT']) > 2 ):
        df.loc[index, 'COUNT'] = np.NAN
    if (float(row['BEGIN_HOUR']) > 17.0):
        df.loc[index, 'BEGIN_HOUR'] = np.NAN
    if (datetime.datetime.strptime(row['DATE'], '%Y-%m-%d') < datetime.datetime(2022, 8, 1)):
        df.loc[index, 'DATE'] = np.NAN

for index, row in df.iterrows():
    df.loc[index, 'COUNT'] = float(row['COUNT'])
    df.loc[index, 'WEEK'] = int(row['WEEK'])
df.dropna(inplace=True)
df = df.drop_duplicates()
df.sort_values(by = 'NAME_STUDENT')
df = df.reset_index()
df = df.drop('index', axis=1)
print(df)