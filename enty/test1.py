import csv

with open('people.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["4","Antony","Danison","Psychology"])