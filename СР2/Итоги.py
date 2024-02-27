import json


with open('scoring.json') as f:
    itogi = json.load(f)
sp = itogi['scoring']
result = 0
for i in range(len(sp)):
    count = 0
    for n in range(len(sp[i]['required_tests'])):
        if input() == 'ok':
            count += 1
    result += count * sp[i]["points"] // len(sp[i]['required_tests'])
print(result)