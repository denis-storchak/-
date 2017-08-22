import serial
from threading import Thread
import Tools
from Tools import addmember

ser = serial.Serial('COM9', 9600, dsrdtr = 1,timeout = None)

file = 'Register_ids.txt'
codes = dict()
dat1 = ''

with open('codenames.txt', 'r') as f:
      for line in f:
            a = line.split()
            us_id, us_name = a[0], a[1:]
            codes[us_id] = us_name

def mySerialDecode():
      
      serialline = ser.readline().split()
      a = str(serialline)[3:-2]
      print(a)

      addmember(file, a)

      if a in codes:      
            dat1 = '11'
      else:
            dat1 = '00'

      data = (bytes(dat1, encoding='ascii'))
      ser.write(data)
      
      return serialline

while True:
      mySerialDecode()

ser.close()
