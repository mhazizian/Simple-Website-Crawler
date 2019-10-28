import json

with open('test1.json') as json_file:
    data = json.load(json_file)
    for obj in data:
        print(obj['link'])