from scipy.fftpack import fft
import numpy as np
import serial
from serial.tools.list_ports import comports as ports
import time
portName = ports()[0][0]
arduino = serial.Serial(port=portName, baudrate=115200, timeout=0.25)

if not arduino.is_open:
    arduino.open()

time.sleep(2.0) #vamo a calmarno
data = []
# Number of sample points
N = 256
while len(data) < N:
    if arduino.in_waiting:
        datum = arduino.readline()
        datum = int(datum.strip())
        data.append(datum)
arduino.close()

# sample spacing
T = 0.05
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(data)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()