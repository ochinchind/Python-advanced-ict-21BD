import pandas as pd 

dict = {
    'Brand' : ['Coca', 'pepsi', 'Sprite', 'water' ],
    'Taste' : [5, 6, 9, 8],
    'Sugar_content' : ['high', 'high', 'high', 'low']
}

df = pd.DataFrame(dict)
print(df)

import csv
with open(r"C:\Users\HP\Downloads\pythgg\Apple.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    df =pd.DataFrame(csvfile, columns = column_names)
    column_names = csvfile._next_()

    for i in csvfile:
        print(i)
print(df)