import serial
import matplotlib.pyplot as plt
seria=serial.Serial(port='COM7',baudrate=115200)
measures=[]
while True:
    try:
        data=str(seria.readline(1000),"UTF-8")
        voltage=0.00488*float(data)
        measures.append(voltage)
    except KeyboardInterrupt:
        lenght=[]
        for i in range(0,len(measures)):
            lenght.append(i)
        plt.plot(lenght,measures)
        plt.xlabel("Time(ms)")
        plt.ylabel("Voltage(V)")
        plt.grid(True)
        plt.show()