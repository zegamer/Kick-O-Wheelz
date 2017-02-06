from key_event import *
import serial
import time

def key_mapping(steer,brake,throttle,nitrous):

##    if(steer<-2):
##        PressKey(DIK_D)
##    if(steer in range(-2,2)):
##        ReleaseKey(DIK_D)
##
##    if(steer>2):
##        PressKey(DIK_A)
##    if(steer in range(-2,2)):
##        ReleaseKey(DIK_A)

##    if(brake==1):
##        PressKey(DIK_S)
##    if(brake==0):
##        ReleaseKey(DIK_S)

    if(throttle==0):
        PressKey(DIK_W)
    if(throttle==1):
        ReleaseKey(DIK_W)
        
##    if(nitrous==1):
##        PressKey(DIK_SPACE)
##    if(nitrous==0):
##        ReleaseKey(DIK_SPACE)

port = "COM4"
baud = 25000

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
