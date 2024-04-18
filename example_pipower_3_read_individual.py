from spc.spc import SPC
from machine import Pin
import time

spc = SPC(bus=0, sda=Pin(0), scl=Pin(1))

def main():
    print(f"Board name: {spc.device.name}")
    print(f"Firmware Version: {spc.read_firmware_version()}")
    time.sleep(2)

    while True:
        print(f"Input voltage: {spc.read_input_voltage()} mV")
        print(f"Raspberry Pi voltage: {spc.read_output_voltage()} mV")
        print(f"Battery voltage: {spc.read_battery_voltage()} mV")
        print(f"Battery percentage: {spc.read_battery_percentage()} %")
        power_source = spc.read_power_source()
        print(f"Power source: {power_source} ({'Battery' if power_source == spc.BATTERY else 'External'})")
        print(f"Input plugged in: {spc.read_is_input_plugged_in()}")
        print(f"Battery plugged in: {spc.read_is_battery_plugged_in()}")
        print(f"Charging: {spc.read_is_charging()}")
        print(f"Shutdown battery percentage: {spc.read_shutdown_battery_percentage()} %")

        print('')
        print(f"Others:")
        shutdown_request = spc.read_shutdown_request()
        shutdown_request_str = 'None'
        if shutdown_request == spc.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = 'None'
        elif shutdown_request == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
            shutdown_request_str = 'Low battery'
        elif shutdown_request == spc.SHUTDOWN_REQUEST_BUTTON:
            shutdown_request_str = 'Button'
        else:
            shutdown_request_str = 'Unknown'
        print(f"Shutdown request: {shutdown_request}({shutdown_request_str})")
        print(f'Board id: {spc.read_board_id()}')
        if ('always_on' in spc.device.peripherals):
            print(f"Always on: {spc.read_always_on()}")
        if ('power_source_voltage' in spc.device.peripherals):
            print(f"Power source voltage: {spc.read_power_source_voltage()} mV")

        print('')
        time.sleep(1)

if __name__ == '__main__':
    main()