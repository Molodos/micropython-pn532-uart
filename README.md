# micropython-pn532-uart
UART based driver for the pn532. This driver is designed for use with micropython on the esp32.

## Status
Just the most basic features are implemented. The primary one is the reading of passive rfid cards.

## References

The code is heavily based on the Adafruit PN532 NFC/RFID control library by Tony DiCola.

__Fork update:__ Forked from https://github.com/infinite-tree/pn532-asyncand, adapted to be synchronous and ready to be used without asyncio dependecy.
