import json

def getConfig():
    data = open("config.json", "r")
    return json.load(data)