from spc.spc import SPC
from machine import Pin, I2C
import time

# For the Raspberry Pi Pico, using I2C(0), pin 0 as SDA, pin 1 as SCL
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

spc = SPC(i2c)

print(f"Board name: {spc.device.name}")
print(f"Firmware Version: {spc.read_firmware_version()}")
print(f"Set shutdown percentage example, shutdown percentage means if it's not charging, and the battery percentage is less than the shutdown percentage, it will give a shutdown request Low Battery, for device to safely shutdown.")
time.sleep(2)
print(f"Shutdown percentage: {spc.read_shutdown_percentage()}%")
time.sleep(2)
print(f"Setting shutdown percentage to 20%")
spc.write_shutdown_percentage(20)
time.sleep(2) # Wait for the shutdown percentage to be updated
current_shutdown_percentage = spc.read_shutdown_percentage()
print(f"Shutdown percentage: {current_shutdown_percentage}%")
if current_shutdown_percentage == 20:
    print("Success")
time.sleep(2)
print(f"Setting shutdown percentage to 10%")
spc.write_shutdown_percentage(10)
time.sleep(2) # Wait for the shutdown percentage to be updated
current_shutdown_percentage = spc.read_shutdown_percentage()
print(f"Shutdown percentage: {current_shutdown_percentage}%")
if current_shutdown_percentage == 10:
    print("Success")
    
time.sleep(2)
print(f"Setting shutdown percentage to 5%")
spc.write_shutdown_percentage(5)
time.sleep(2) # Wait for the shutdown percentage to be updated
current_shutdown_percentage = spc.read_shutdown_percentage()
print(f"Shutdown percentage: {current_shutdown_percentage}%")
if current_shutdown_percentage == 5:
    print("Success")
else:
    print("Failed, shutdown percentage minimal is 10%")
