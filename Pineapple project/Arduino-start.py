import serial
import os
import sys
 
#��������� ����
ser = serial.Serial('COM9', 9600, dsrdtr = 1,timeout = 0)
 
#���������� ��� ������ ��� ������ �� ������ ���������
prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
f1 = open(prgpath + "\\data1.log", "a")
f5 = open(prgpath + "\\data5.log", "a")
 
#��������� ������ � ������������� ������ �� �����
def mySerialDecode():
       
      code = []
      data = "0"
      command = "command"
      unitID = "0"
 
      time.sleep(0.2)      
      serialline = ser.readline().split('\n')
       
      if serialline[0]:
 
            mydata = serialline[0]
            code = mydata.split(',')
            unitID = code[0]
            command = code[1]
            data = code[2]
                   
      return unitID, command, data
 
#������������� ������
def mySwitch():
      code = mySerialDecode()
      unitID = int(code[0])
      data = code[2]
       
      if unitID == 001:
            f1.write(data)
            f1.write('\n')
            print data
             
      elif unitID == 005:
            f5.write(data)
            f5.write('\n')
            print data
      else:
            pass
 
#��������� �������� ������ � ����
#��������� ���������� (����)
def ledON():
      ser.write('Y') 
      print 'led ON'
 
#����� �������� ���-�� � ����
def ledON()
 
#�������� ���� ���������
while 1:
       
      #������ ������ �� ����� � ������������� �� ������
      try:
            mySwitch()
 
      #����� �� Ctrl+C
      except KeyboardInterrupt:
            break
 
      
#��������� ���������
ser.write("N")
print 'led OFF'
 
#��������� ����
ser.close()
 
#��������� �����
f1.close()
f5.close()