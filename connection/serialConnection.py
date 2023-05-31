import serial
import time

class serialConnection:

    def __init__(self, userport, userbaud):
        self.puerto = serial.Serial(port = userport,
                                    baudrate = userbaud,
                                    bytesize = serial.EIGHTBITS,
                                    parity   = serial.PARITY_NONE,
                                    stopbits = serial.STOPBITS_ONE)
    
    def sendData(self, data, delay = 1):
        try:
            self.puerto.write(data.encode())
            time.sleep(delay)

        except serial.SerialException:
            print('El puerto no esta disponible')

        except serial.portNotOpenError:
            printl('El puerto no esta abierto')

    def retriveData(self):
        return self.puerto.readline()


    def closeConnection(self):
        self.puerto.close()
