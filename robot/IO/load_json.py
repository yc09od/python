import json

class server_config:
    hostname = ''
    port = 0

    def __init__(self, d):
        self.__dict__ = d

f = open("data.json", "r")

content = f.read()

j = json.loads(content)
config = server_config(j)
print(config.hostname)
print(config.port)
