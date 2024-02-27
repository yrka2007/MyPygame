import json
import csv

with open('guests.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=';', quotechar='|')
    for i in reader:
        if 'lilac' in i[-2]:
            lord = {"name": i[1], 'title': i[2], 'eye_color': i[3]}
            print(lord)
with open('lubbocks.json', 'w') as file:
    json.dump(lord, file)

