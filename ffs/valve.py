from ffs.relay import WaveshareRelayHat
from ffs.handlers import UDP
import time


class Valve():
    def __init__(self, relay_pin: int, udp_ip: str, udp_port: (int,str)) -> None:
        self.relay_pin = relay_pin
        self.relay = WaveshareRelayHat()  # Set up the relay hat.
        self.relay.initialize(self.relay_pin)
        self._udp = UDP(ip = udp_ip, port = udp_port)

    def enable_fsw(self):
        self.relay.enable(self.relay_pin)

    def enable_tsw(self):
        self.relay.disable(self.relay_pin)

    def send_state(self):
        if self.relay.state(self.relay_pin) is True:
            self._udp.send_info('FSW')
        elif self.relay.state(self.relay_pin) is False:
            self._udp.send_info('TSW')

    def run_fsw(self,num_min: (int,float)) -> None:
        self.enable_fsw()
        self._udp.send_debug('Starting FSW cycle...')
        time.sleep(num_min * 60)
        self.enable_tsw()
        self._udp.send_debug('FSW cycle complete.')


    def closeout(self) -> None:
        """
        Closeout the valve by deinitializing the relay hat.
        :return: None
        """
        self.relay.deinitialize()
        self._udp.send_debug("Relay and valve operations exited successfully. Available for next operation.")

    def __enter__(self):
        """Context manager for those who want to wrap everything in a with statement."""
        return self

    def __exit__(self,t, v, tb):
        self.closeout()