import json

f = open("data.json", "r")

content = f.read()

print(content)
j = json.loads(content)
print(j['hostname'])
