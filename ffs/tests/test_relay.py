from flowthrough_valve.relay import WaveshareRelayHat, WaveshareDefaultChannels
import time

channels = [WaveshareDefaultChannels.One, WaveshareDefaultChannels.Two, WaveshareDefaultChannels.Three]

def main():
    no_context()   # Test Relay class functionality with no context.
    context()  # Test RelayHat class functionality with context.


def no_context():
    relay = WaveshareRelayHat()
    for channel in channels:
        relay.initialize(channel)
        relay.enable(channel)
        time.sleep(3)
        if relay.state(channel) is True:
            relay.disable(channel)
        else:
            raise RuntimeError("A relay channel did not enable when it was told to enable!")
    relay.deinitialize()


def context():
    with WaveshareRelayHat() as relay:
        for channel in channels:
            relay.enable(channel)
            time.sleep(3)
            if relay.state(channel) is True:
                relay.disable(channel)
            else:
                raise RuntimeError("A relay channel did not enable when it was told to enable!")


def test_answer():  # Test for pytest.
    relay = WaveshareRelayHat()
    for channel in channels:
        relay.initialize(channel)
        assert relay.state(channel) is False
    relay.deinitialize()

if __name__ == "__main__":
    main()