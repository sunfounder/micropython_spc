from spc.spc import SPC
from machine import Pin, I2C
import time

# For the Raspberry Pi Pico, using I2C(0), pin 0 as SDA, pin 1 as SCL
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

shutdown_signal = Pin(2, Pin.OUT)
shutdown_signal.value(0)

spc = SPC(i2c)


def main():
    print(f"Board name: {spc.device.name}")
    print(f"Firmware Version: {spc.read_firmware_version()}")
    print(f"Shutdown when request example, wait until battery dying or hold button 2 seconds then release.")
    time.sleep(2)

    while True:
        shutdown_request = spc.read_shutdown_request()
        if shutdown_request != spc.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = ''
            if shutdown_request == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
                shutdown_request_str = 'Low battery'
            elif shutdown_request == spc.SHUTDOWN_REQUEST_BUTTON:
                shutdown_request_str = 'Button'
            else:
                shutdown_request_str = 'Unknown'
            print(f"Shutdown request: {shutdown_request}({shutdown_request_str})")
            print('Shutting down...')
            # Do whatever you need to do before shutting down
            shutdown_signal.value(1)

        time.sleep(1)

if __name__ == '__main__':
    main()
