import csv
import json

csvfile = open('output.csv', 'r')
jsonfile = open('parsed.json', 'w')

fieldnames = ("tag","patterns","responses")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('{"intents": [')

counter = 0
for row in reader:
    counter += 1

csvfile.close()
csvfile = open('output.csv', 'r')
reader = csv.DictReader( csvfile, fieldnames)

rowCounter = 0
for row in reader:
    if rowCounter != 0:
        json.dump(row, jsonfile)
        print(row)
        if rowCounter != (counter-1):
            jsonfile.write(',\n')
    
    rowCounter += 1
    
jsonfile.write(']}')

csvfile.close()
jsonfile.close()