import serial
import os
import sys
 
#открываем порт
ser = serial.Serial('COM9', 9600, dsrdtr = 1,timeout = 0)
 
#подготовка лог файлов для данных от разных устройств
prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
f1 = open(prgpath + "\\data1.log", "a")
f5 = open(prgpath + "\\data5.log", "a")
 
#процедура чтения и декодирования строки из порта
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
 
#маршрутизация данных
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
 
#процедура передачи данных в порт
#включение светодиода (тест)
def ledON():
      ser.write('Y') 
      print 'led ON'
 
#проба записать что-то в порт
def ledON()
 
#основной цикл программы
while 1:
       
      #запуск чтения из порта и маршрутизация по файлам
      try:
            mySwitch()
 
      #выход по Ctrl+C
      except KeyboardInterrupt:
            break
 
      
#выключаем светодиод
ser.write("N")
print 'led OFF'
 
#закрываем порт
ser.close()
 
#закрываем файлы
f1.close()
f5.close()