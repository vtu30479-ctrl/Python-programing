import csv
with open('apple_quality.csv','r') as file:
    data=csv.reader(file)
    for row in data:
        print(row)
