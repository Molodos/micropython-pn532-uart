# micropython-pn532-uart
UART based driver for the pn532. This driver is designed for use with micropython on the RP2040 Zero.

## Status
Just the most basic features are implemented. The primary one is the reading of passive rfid cards.

## Usage

```python
from pn532 import PN532Uart
import utime

DEBUG = False

try:
    rf = PN532Uart(1, tx=4, rx=5, debug=DEBUG)
    rf.SAM_configuration()
    ic, ver, rev, support = rf.get_firmware_version()
    print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
except Exception as e:
    rf = None
    print('No NFC reader (PN532) detected')

while rf is not None:
    try:
        uid = rf.read_passive_target()
        print("Card UUID: " + ''.join('{:02x}'.format(x) for x in uid))
    except Exception as e:
        print('timeout!')
```

## References

The code is heavily based on the Adafruit PN532 NFC/RFID control library by Tony DiCola.

__Fork update:__ Forked from https://github.com/insighio/micropython-pn532-uart, adapted to work on the RP2040 Zero.
