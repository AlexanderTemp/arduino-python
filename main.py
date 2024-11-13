import serial
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 9600) # Modificar según puerto salida COM3

plt.ion()
fig, ax = plt.subplots()

while True: 
  try: 
    line = ser.readline().decode('utf-8').rstrip()
    if line: 
      print(line)
      
  except KeyboardInterrupt: 
    break

ser.close()
