import csv
from  import datatime

temp = {}
with open('noname.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=";",)
        temp = next(reader)

print(temp)