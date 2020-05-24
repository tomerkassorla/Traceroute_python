import sys
import time

i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *

sys.stdin, sys.stdout, sys.stderr = i, o, e


def main():
    ok = True
    i = 1
    while ok:
        tracert_packet = IP(ttl=i, dst="www.google.com") / ICMP()
        start_time = int(round(time.time() * 1000))
        request_packet = sr1(tracert_packet, verbose=0, timeout=1)
        end_time = int(round(time.time() * 1000))
        if request_packet is None:
            print ' ' + str(i) + " : " + "*          *           *"
        else:
            print ' ' + str(i) + " : " + request_packet[IP].src + ', time : ' + str(end_time - start_time) + ' ms'
            if request_packet[ICMP].type == 0:
                ok = False
        i += 1


if __name__ == '__main__':
    main()