import time
import serial
import os
import socket
import struct
from voice_engine.source import Source
from voice_engine.channel_picker import ChannelPicker
from voice_engine.kws import KWS
from voice_engine.doa_respeaker_6p1_mic_array import DOA
from pixel_ring import pixel_ring
#from gpiozero import LED

TCP_IP='192.168.43.195'#IP address
TCP_PORT=5006
BUFFER_SIZE=1024
MESSAGE="HELLO,WORLD!"

s= socket.socket()
s.bind(('192.168.43.195',TCP_PORT))
s.listen(5)
def main():
    #power = LED(5)
    #power.on()
    #ard = serial.Serial()
    #ard.open()
    src = Source(rate=16000, channels=8)
    ch1 = ChannelPicker(channels=8, pick=1)
    kws = KWS()
    doa = DOA(rate=16000)
#pixel_ring.set_brightness(20)
    #pixel_ring.change_pattern('echo')
    #pixel_ring.wakeup()
    src.link(ch1)
    ch1.link(kws)
    src.link(doa)
    time.sleep(1)
	def on_detected(keyword):
        direction = doa.get_direction()
        #pixel_ring.think()
        #time.sleep(1)
        print('detected {} at direction {}'.format(keyword, direction))
        c.send(str(direction))
        #if (direction >= 0) and (direction <= 180):
            #ard.write(struct.pack('>B', 180-direction))
            #c.send(str(direction))
	c, addr = s.accept()
	kws.set_callback(on_detected)       

	src.recursive_start()
   	while True:
        #c, addr = s.accept()
        try:
            #dire = doa.get_direction()
            #print(dire)
            #c.send('dire')
            time.sleep(1)
        except KeyboardInterrupt:
            break
    c.close()
    src.recursive_stop()
if __name__ == '__main__':
    main()


