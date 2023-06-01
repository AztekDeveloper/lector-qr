from querys import query_api 
from connection import serialConnection
from functions.config import getConfig

def main():
    config = getConfig()
    lectorConnection = serialConnection.serialConnection(config['serial'], config['baudrate'])
    print(config['serial'], config['baudrate'])
    while(True):
        try:
            print("Entra")
            data = lectorConnection.retriveData()
            print('data: ', str(data))
            data = str(data).split('/')[9].split('\\')[0]
            print('ticket: ' + data)
            validateTicket(query_api.get_ticket_info(data).json())
        except IndexError:
            print("Error en la lectura del codigo qr. Por favor acerque de nuevo el codigo")        

def validateTicket(ticketData):
    print(json.dumps(ticketData)['error'])

main()