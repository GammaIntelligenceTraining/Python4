import json

with open('sample.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    print(data['quiz']['sport']['q1']['question'])