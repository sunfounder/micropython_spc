from spc.spc import SPC
from machine import Pin
import time

spc = SPC(bus=0, sda=Pin(0), scl=Pin(1))

def main():
    print(f"Board name: {spc.device.name}")
    print(f"Firmware Version: {spc.read_firmware_version()}")
    time.sleep(2)

    while True:
        # Read the data before clearing the screen，to retain the last data when an error occurs.
        data_buffer = spc.read_all()

        print(f"Input voltage: {data_buffer['input_voltage']} mV")
        print(f"Output voltage: {data_buffer['output_voltage']} mV")
        print(f"Battery voltage: {data_buffer['battery_voltage']} mV")
        print(f"Battery percentage: {data_buffer['battery_percentage']} %")
        print(f"Power source: {data_buffer['power_source']} ({'Battery' if data_buffer['power_source'] == spc.BATTERY else 'External'})")
        print(f"Input plugged in: {data_buffer['is_input_plugged_in']}")
        print(f"Battery plugged in: {data_buffer['is_battery_plugged_in']}")
        print(f"Charging: {data_buffer['is_charging']}")
        print(f"Shutdown battery percentage: {data_buffer['shutdown_battery_percentage']} %")

        print('')
        print(f"Internal data:")
        shutdown_request_str = 'None'
        if data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_NONE:
            shutdown_request_str = 'None'
        elif data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_LOW_BATTERY:
            shutdown_request_str = 'Low battery'
        elif data_buffer['shutdown_request'] == spc.SHUTDOWN_REQUEST_BUTTON:
            shutdown_request_str = 'Button'
        else:
            shutdown_request_str = 'Unknown'
        print(f"Shutdown request: {data_buffer['shutdown_request']}({shutdown_request_str})")
        print(f'Board id: {spc.read_board_id()}')
        if ('always_on' in spc.device.peripherals):
            print(f"Always on: {spc.read_always_on()}")
        if ('power_source_voltage' in spc.device.peripherals):
            print(f"Power source voltage: {spc.read_power_source_voltage()} mV")

        print('')
        print('')
        time.sleep(1)

if __name__ == '__main__':
    main()