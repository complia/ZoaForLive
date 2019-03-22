import time
import rtmidi_python as rtmidi
import numpy as np

# TODO: Put this in a settings file
YAW_CC = 10
PITCH_CC = 11
ROLL_CC = 12

FRAMERATE = 30

CC_HEX = 0xb0

# Setup midi
midi_out = rtmidi.MidiOut(b'in')
midi_port = midi_out.ports[0]
midi_out.open_port(midi_port)

while True:
    t = time.time()

    pitch = 127*0.5*(1 + np.sin(t))
    yaw = 127*0.5*(1 + np.sin(t - (1/3.0)*2*np.pi))
    roll = 127*0.5*(1 + np.sin(t - (2/3.0)*2*np.pi))    

    midi_out.send_message([CC_HEX, YAW_CC, pitch])
    midi_out.send_message([CC_HEX, PITCH_CC, yaw])
    midi_out.send_message([CC_HEX, ROLL_CC, roll])

    time.sleep(1.0/FRAMERATE)
