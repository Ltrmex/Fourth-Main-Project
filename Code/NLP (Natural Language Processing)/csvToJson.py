import csv
import json

csvfile = open('C:/Users/Ltrmex/Desktop/Fourth-Main-Project/output.csv', 'r')
jsonfile = open('C:/Users/Ltrmex/Desktop/Fourth-Main-Project/parsed.json', 'w')

fieldnames = ("tag","patterns","responses")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')