from querys import query_api 
from connection import serialConnection
import json

def main():
    #print(query_api.get_ticket_info('3D00461E197C').json())
    getConfig()
    lectorConnection = serialConnection.serialConnection('/dev/ttyUSB0', 9600)
    while(True):
        print(lectorConnection.retriveData())

def getConfig():
    data = open("config.json", "r").read()
    print(json.load(data))

main()