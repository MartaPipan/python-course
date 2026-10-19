import csv
import pandas as pd

link_to_file=input("enter file name")
with open('./people.csv', 'r') as file:
    reader=csv.reader(file)


for row in reader:
    print(row)
