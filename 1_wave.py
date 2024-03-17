import pyaudio
import numpy as np 
import matplotlib as mpl 
mpl.use('TkAgg')
import matplotlib.pyplot as plt 

# quit by key q function
def on_press(event):
    global stream, p, END
    if event.key == 'q':
        plt.close()
        stream.stop_stream()
        stream.close()
        p.terminate()
        END = True

END = False
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNEL = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNEL,rate=RATE, input=True,frames_per_buffer=CHUNK)

# Visualize the data
mpl.rcParams['toolbar'] = 'None'
fig, ax = plt.subplots(figsize=(12,3))

# Quit by key q
fig.canvas.mpl_connect('key_press_event', on_press)

plt.subplots_adjust(left=0.001,top=0.999,right=0.999,bottom=0.001)
plt.get_current_fig_manager().set_window_title('Wave')
x = np.arange(0,CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK),color='#C04851')
ax.set_xlim(0,CHUNK-1)
ax.set_ylim(-2**15,2**15)

plt.axis('off')
plt.ion()
plt.show()

while END == False:
    data = stream.read(CHUNK,exception_on_overflow=False)
    data = np.frombuffer(data,dtype=np.int16)
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)
    # print(data)
