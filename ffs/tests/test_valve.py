from flowthrough_valve.valve import Valve
from flowthrough_valve.relay import WaveshareDefaultChannels as Channel

def main():

    valve = Valve(Channel.One, udp_ip = "172.20.230.223", udp_port = "30321")
    valve.run_fsw(10/60)
    valve.closeout()

if __name__ == "__main__":
    main()