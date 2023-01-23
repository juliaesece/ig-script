import csv
import json

nameFile = input('Enter name of file without json : ')

nameFileJson = nameFile + ".json"

f = open(nameFileJson)
accountsInt = json.load(f)
f.close()

newFileName = nameFile + ".csv"

keys = accountsInt[0].keys()

with open(newFileName, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(accountsInt)
    

