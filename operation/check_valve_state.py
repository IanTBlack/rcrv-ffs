from ffs.valve import Valve
from ffs.relay import WaveshareDefaultChannels as Channel
import sys
import time


def main():
    seconds_between_messages = float(sys.argv[1])
    udp_ip = str(sys.argv[2])
    udp_port = str(sys.argv[3])
    valve = Valve(Channel.One, udp_ip, udp_port)
    while True:
        start = time.monotonic()
        valve.send_state()
        end = time.monotonic()
        time.sleep(seconds_between_messages-(end-start))


if __name__ == "__main__":
    main()