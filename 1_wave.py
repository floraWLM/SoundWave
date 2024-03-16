import pyaudio
import numpy as np 
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNEL = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNEL,rate=RATE, input=True,frames_per_buffer=CHUNK)

# Visualize the data
fig, ax = plt.subplots(figsize=(12,3))
x = np.arange(0,CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK),color='#C04851')
ax.set_xlim(0,CHUNK-1)
ax.set_ylim(-2**15,2**15)

plt.ion()
plt.show()

while True:
    data = stream.read(CHUNK,exception_on_overflow=False)
    data = np.frombuffer(data,dtype=np.int16)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)
    # print(data)
