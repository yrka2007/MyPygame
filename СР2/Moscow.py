from zipfile import ZipFile
import json

with ZipFile('input.zip') as zipf:
    count = 0
    for file in zipf.filelist:
        if ".json" == file.filename[-5:]:
            with zipf.open(file.filename, 'r') as jsf:
                data = jsf.read().decode('utf8')
                d = json.loads(data)
                if d.get('city') == 'Москва':
                    count += 1
print(count)
