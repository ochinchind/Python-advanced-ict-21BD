#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import datetime
import csv
import pandas as pd

lists = [[] for i in range(7)]

with open(r"C:\Users\HP\Downloads\GD.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        for i in range(0, len(row)): lists[i].append(row[i])
            
for i in range(1,6):
    lists[i] = [float(j) for j in  lists[i] ]
    
lists[0] = [datetime.datetime.strptime(j, "%Y-%m-%d") for j in  lists[0] ]



print(lists)