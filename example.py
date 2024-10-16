import machine
from pn532 import PN532Uart
import utime

# This example initializes the PN532 and then enters a forever loop
# waiting for rfid tags to be read.
#
# Pinout:
#      esp32 tx = 22 = pn532 rx
#      esp32 rx = 23 = pn532 tx
#
#      esp32 OUT = 21 = buzzer (or led)
#

DEBUG = False


def test():
    buzzer = machine.Pin(21, machine.Pin.OUT)
    buzzer.off()

    # NOTE: on several of the esp32-wrover dev boards, the default uart2 pins
    #       conflict with the psRam so the pn532 is plugged into two unused
    #       pins instead.
    try:
        rf = PN532Uart(2, tx=22, rx=23, debug=DEBUG)
        rf.SAM_configuration()
        ic, ver, rev, support = rf.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
    except Exception as e:
        rf = None
        print('No NFC reader (PN532) detected')

    while rf is not None:
        try:
            uid = rf.read_passive_target()
            print("Card UUID: ", [hex(i) for i in uid])
            buzzer.on()
            utime.sleep_ms(200)
            buzzer.off()
        except Exception as e:
            # NOTE: This is important to stop the reader from reporting cards after
            #       we are no longer waiting.
            rf.release_targets()
            print('timeout!')

test()
