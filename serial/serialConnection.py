import serial
import time
import inspect

class serialConnection:

    def __init__(self):
        self.puerto = serial.Serial(port = '/dev/ttyUSB0',
                                    baudrate = 9600,
                                    bytesize = serial.EIGHTBITS,
                                    parity   = serial.PARITY_NONE,
                                    stopbits = serial.STOPBITS_ONE)
    
    def sendData(self, data):
        try:
            self.puerto.write(data.encode())
            time.sleep(5)

        except serial.SerialException:
            print('El puerto no esta disponible')

        except serial.portNotOpenError:
            printl('El puerto no esta abierto')
            print('Fin del script')

    #def retriveData(self, data):


    def closeConnection(self):
        self.puerto.close()
