from querys import query_api 
import serial

def main():
    print(query_api.get_ticket_info('3D00461E197C').json())
    lector = serial.Serial('dev/ttyUSB0', 9600)
    while(True):
        print(lector.read())

main()
