import csv

with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimeter='', quotechar='|')
    for row in spamreader:
        print(','.join(row))