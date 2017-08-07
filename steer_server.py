import socket
from key_event import *
import time,sys

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    port = 1234
    IP = getAddrIP()
    sock.bind((IP,port))

    print 'started on',IP,'with Port #', port
    print 'now run the Directx game and make sure the game is in the foreground';
    
    try:    
        while True:

            data,addr = sock.recvfrom(16)
            data = data.split()
            steer = -1*float(data[0])
            thr = float(data[1])
            brk = float(data[2])
            nit = float(data[3])
            
            print " Steer : " + str(steer) + " Throttle : " + str(thr) + " Brake : " + str(brk) + " Nit : " + str(nit)

            if(steer > 2.0):
                PressKey(DIK_D)
            if steer in range(-1,1):
                ReleaseKey(DIK_D)

            if(steer < -2.0):
                PressKey(DIK_A)
            if steer in range(-1,1):
                ReleaseKey(DIK_A)

            if thr == 1:
                PressKey(DIK_W)
            if thr == 0:
                ReleaseKey(DIK_W)

            if brk == 1:
                PressKey(DIK_S)
            if brk == 0:
                ReleaseKey(DIK_S)

            if nit == 1:
                PressKey(DIK_SPACE)
            if nit == 0:
                ReleaseKey(DIK_SPACE)

    except:
        print ' Exiting ... '
        time.sleep(1)
        socket.close()
        sys.exit()


def getAddrIP():
##    Enter that ip shown at ipconfig/all > Ethernet via Ethernet > IPV4
##    That is in case this below function does not resolve.
    return socket.gethostbyname(socket.getfqdn())


if __name__=='__main__':
    start_server()

