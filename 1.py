import csv
import json 

Date = []
Open=[]
High=[]
Low = []
Close = []
AdjClose = []
Volume = []
with open("C:/Users/HP/Downloads/GD.csv", 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        Date.append(row[0])
        Open.append(row[1])
        High.append(row[2])
        Low.append(row[3])
        Close.append(row[4])
        AdjClose.append(row[5])
        Volume.append(row[6])
    
for i in range(len(Date)):
    print(Date[i], " | ", Open[i], " | ", High[i], " | ", Low[i], "|", Close[i], "|", AdjClose[i], "|", Volume[i], "|")
    
mydict = []
mydict = [name.upper() for name in mydict]
for i in range(len(Date)):
    mydict.append({Date[i],Open[i],High[i],Low[i],Close[i],AdjClose[i],Volume[i]})
with open('GDstructured.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    for i in range(len(Date)):
        writer.writerows(mydict)

