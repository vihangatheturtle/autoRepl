from datetime import datetime
import socket
import time
import sys

IPADDR = '86.24.92.243'
PORTNUM = 80

PACKETDATA = b'f1a525da11f6'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

def tryConnect():
    try:
        s.connect((IPADDR, PORTNUM))
    except Exception as ex:
            print(f"Excepted at: {datetime.now()} :: {type(ex)} :: Exception occured whilst trying to connect (IP: '{IPADDR}', PORT: '{PORTNUM}', ERROR: '{ex}, EXCEPTION ARGS: '{ex.args}'')")
            time.sleep(1)
            tryConnect()
       
tryConnect()
        
while True:
    try:
        s.send(PACKETDATA)
        print(f"Packet successfully sent, packet data: '{PACKETDATA.decode()}', packet size: '{len(PACKETDATA) * 8} bytes', sent at: '{datetime.now()}'")
    except Exception as ex:
        print(f"Excepted at: {datetime.now()} :: {type(ex)} :: Exception occured whilst trying to send UDP packet (BINARYDATA: '{PACKETDATA.decode()}',IP: '{IPADDR}', PORT: '{PORTNUM}', ERROR: '{ex}', EXCEPTION ARGS: '{ex.args}')")
        time.sleep(1)
