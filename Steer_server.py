from key_event import *
import serial
import time

def key_mapping(steer,brake,throttle,nitrous):
    if(steer<1):
        PressKey(DIK_D)
    elif(steer in range(-1,1)):
        ReleaseKey(DIK_D)

    if(steer>1):
        PressKey(DIK_A)
    elif(steer in range(-1,1)):
        ReleaseKey(DIK_A)

    if(brake):
        PressKey(DIK_S)
    else:
        ReleaseKey(DIK_S)

    if(throttle==1):
        PressKey(DIK_W)
    else:
        ReleaseKey(DIK_W)
        
    if(nitrous==1):
        PressKey(DIK_SPACE)
    else:
        ReleaseKey(DIK_SPACE)

port = "COM5"
baud = 19200

ser = serial.Serial(port,baud)

try:
    counter = 0
    while True:
        data = ser.readline()
        if counter < 2:
            counter = counter+1
            continue
        print ' Loop : ',
        if data:
            data = data.split()
            steer = int(data[0])
            brake = int(data[1])
            throttle = int(data[2])
            nitrous = int(data[3])
            key_mapping(steer,brake,throttle,nitrous)
            print str(steer) + " " + str(brake) + " " + str(throttle) + " " + str(nitrous)

    ser.close()

except:
    print 'Error'
    ser.close()
    time.sleep(2)
