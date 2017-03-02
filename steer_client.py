import RPi.GPIO as GPIO
import mpu6050
import socket
from time import sleep
from sys import exit

thr_pin = 26
brk_pin = 19
nitr_pin = 13

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = raw_input("Enter the ip shown at server : ")
port = raw_input("Enter port shown at server : ")
address = (ip,port)

address = (address)

try:
    sock.connect(address)
    print ' Connected to \tIP : ' + str(address[0]) + "\t port : " + str(address[1])
except:
    print ' Connection failed ... '
    sleep(2)
    exit()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(thr_pin, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(brk_pin, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(nitr_pin, GPIO.IN,GPIO.PUD_DOWN)

acc = mpu6050.mpu6050(0x68)

acc.read_accel_range(16)

accel_data = acc.get_accel_data()

xi = accel_data['x']

try:
    while True:
        
        data = ""
        accel_data = acc.get_accel_data()
s
        steer = int(accel_data['x'] - xi)
        thr = GPIO.input(thr_pin)
        brk = GPIO.input(brk_pin)
        nitr = GPIO.input(nitr_pin)

        data = str(steer)+ " " + str(thr) + " " + str(brk) + " " + str(nitr)

        sock.sendto(data,address)

        print data

finally:
    GPIO.cleanup()
