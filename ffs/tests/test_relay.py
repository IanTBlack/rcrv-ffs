from ffs.relay import WaveshareRelayHat, WaveshareDefaultChannels
import pytest
import time


def no_context():
    relay = WaveshareRelayHat()
    for channel in channels:
        relay.initialize(channel)
        relay.enable(channel)
        time.sleep(1)
        if relay.state(channel) is True:
            relay.disable(channel)
        else:
            raise RuntimeError("A relay channel did not enable when it was told to enable!")
    relay.deinitialize()


def context():
    with WaveshareRelayHat() as relay:
        for channel in channels:
            relay.enable(channel)
            time.sleep(1)
            if relay.state(channel) is True:
                relay.disable(channel)
            else:
                raise RuntimeError("A relay channel did not enable when it was told to enable!")


channels = [WaveshareDefaultChannels.One, WaveshareDefaultChannels.Two, WaveshareDefaultChannels.Three]
no_context()   # Test Relay class functionality with no context.
context()  # Test RelayHat class functionality with context.


def test_answer():  # Test for pytest.
    relay = WaveshareRelayHat()
    for channel in channels:
        relay.initialize(channel)
        assert relay.state(channel) is False
    relay.deinitialize()

