from ffs.valve import Valve
from ffs.relay import WaveshareDefaultChannels as Channel
import sys


def main():
    run_filtered_min = float(sys.argv[1])  # Pull the number of minutes that the valve should be run for from the CLI.
    udp_ip = str(sys.argv[2])
    udp_port = str(sys.argv[3])
    valve = Valve(Channel.One, udp_ip, udp_port)
    valve.run_fsw(run_filtered_min)
    valve.closeout()

if __name__ == "__main__":
    main()