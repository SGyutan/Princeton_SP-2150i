"""
Created on 04 November 2021

Princeton instruments SP-2150i Command program
https://www.princetoninstruments.com/wp-content/uploads/2020/04/SP-2150i.pdf

RS-232 computer port must be set up as follows:  
9600 baud, 8 data bits, no parity, 1 start bit, 1 stop bit.  

com is comport number. 
    Windows example: com = 'COM2'
    Linux example: com = '/dev/ttyUSB0'

Rython: 3.7 over
Requiremnt module: pyserial

"""

import serial

class Acton():

    def __init__(self, com:str, baudr=9600):
        self.com = com
        self.baudr = baudr
        
    def get_nm(self): 
        with serial.Serial(port=self.com) as ser:
            ser.write(b'?NM\r')
            self.curr_nm = ser.read_until().decode().split()
        return self.curr_nm
    
    def get_nm_per_min(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'?NM/MIN\r')
            self.curr_nm_min = ser.read_until().decode().split()
        return self.curr_nm_min

    def get_serial(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'SERIAL\r')
            self.serial_no = ser.read_until().decode().split()
        return self.serial_no
    
    def get_model(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'Model\r')
            self.model_no = ser.read_until().decode().split()
        return self.model_no

    def get_turret(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'?TURRET\r')
            self.turret = ser.read_until().decode().split()
        return self.turret

    def get_filter(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'?FILTER\r')
            self.filter = ser.read_until().decode().split()
        return self.filter

    def get_grating(self):
        with serial.Serial(port=self.com) as ser:
            ser.write(b'?GRATING\r')
            self.grating = ser.read_until().decode().split()
        return self.grating
    
    def goto_nm(self, nm:float):
        with serial.Serial(port=self.com) as ser:
            command = (f'{nm:.1f} GOTO\r').encode()
            ser.write(command)
            goto = ser.read_until().decode().split()
            print(goto)
    
    def set_turret(self,num:int):
        with serial.Serial(port=self.com) as ser:
            if num <=2:
                command = (f'{int(num)} TURRET\r').encode()
                ser.write(command)
                turret_set = ser.read_until().decode().split()
                print(turret_set)
            else:
                print("There is not turret with this input")
        
    def set_filter(self,num:int):
        with serial.Serial(port=self.com) as ser:        
            if num <=6:
                command = (f'{int(num)} FILTER\r').encode()
                ser.write(command)
                filter_set = ser.read_until().decode().split()
                print(filter_set)  
            else:
                print("There is no filter with this input")
        
    def set_grating(self,num:int):
        with serial.Serial(port=self.com) as ser:
            if num <=2:
                command = (f'{int(num)} GRATING\r').encode()
                ser.write(command)
                grating_set = ser.read_until().decode().split()  
                print(grating_set)
            else:
                print("There is no grating with this input")
        

if __name__ == '__main__':
    
    acton = Acton('COM5')
    
    acton_prop=[acton.get_nm(),
          acton.get_nm_per_min(),
          acton.get_filter(),
          acton.get_grating(),
          acton.get_serial(),
          acton.get_model(),
          acton.get_turret()]
    print(acton_prop)
    print('-'*5)
    
    # print(acton.get_nm())
    # nm=1000
    # acton.goto_nm(nm)
    # print(acton.get_nm())
    
    # print(acton.get_grating())
    # acton.set_grating(2)
    # print(acton.get_grating())
    
 