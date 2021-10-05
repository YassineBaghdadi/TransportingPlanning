import os, json

server = json.load(open(os.path.join(os.getcwd(), "server.json")))

print(server["host"])