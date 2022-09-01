import RPi.GPIO as GPIO
import time

class WaveshareDefaultChannels:
    """A class that denotes the default channel raspberry pi pins when the jumpers are installed on the Relay Hat."""
    One: int = 26
    Two: int = 20
    Three: int = 21


class WaveshareRelayHat():
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)

    def initialize(self, relay_pin: int , initial_pin_state: int = 1) -> None:
        """
        By default, pins in the 0 state will flip a relay.
        Setting the initial to 1 ensures they do not flip at start.
        """
        GPIO.setup(relay_pin, GPIO.OUT, initial = initial_pin_state)

    def enable(self, relay_pin: int) -> None:
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(0.01)

    def disable(self, relay_pin: int) -> None:
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(0.01)

    def state(self, relay_pin: int) -> bool:
        """
        Obtain a relay state. If True, the relay is enabled. If False it is disabled. Relay state is opposite
        of pin state.

        :param relay_position: An integer or an attribute of the Relay class. The pin for controlling the relay channel.
        :return:
        """
        pin_state = bool(GPIO.input(relay_pin))
        if pin_state is True:
            relay_state = False
        elif pin_state is False:
            relay_state = True
        return relay_state

    def deinitialize(self) -> None:
        """
        Deinitialize everything and cleanup the pins.
        :return: None
        """
        GPIO.cleanup()

    def __enter__(self) -> object:
        """Context Manager. Allows for wrapping of the Relay() class into a with statement."""
        self.initialize(Channel.One)
        self.initialize(Channel.Two)
        self.initialize(Channel.Three)
        return self

    def __exit__(self,t,v,tb) -> None:
        """Context Manager. Allows for wrapping of the Relay() class into a with statement."""
        self.deinitialize()







