from pn532 import PN532Uart


def test():

    # Version for RP2040 Zero
    try:
        rf = PN532Uart(1, tx=4, rx=5, debug=false)
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
        except Exception as e:
            # NOTE: This is important to stop the reader from reporting cards after
            #       we are no longer waiting.
            rf.release_targets()
            print('timeout!')

test()
