from spc.spc import SPC
from machine import Pin, I2C
import time

# For the Raspberry Pi Pico, using I2C(0), pin 0 as SDA, pin 1 as SCL
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

spc = SPC(i2c)

print(f"Board name: {spc.device.name}")
print(f"Firmware Version: {spc.read_firmware_version()}")
print(f"Set power off percentage example, power off percentage means when battery percentage is less than the power off percentage, the device will cut off the power to protect battery.")
time.sleep(2)
print(f"Power off percentage: {spc.read_power_off_percentage()}%")
time.sleep(2)
print(f"Setting power off percentage to 20%")
spc.write_power_off_percentage(20)
time.sleep(2) # Wait for the power off percentage to be updated
current_power_off_battery_percentage = spc.read_power_off_percentage()
print(f"Power off percentage: {current_power_off_battery_percentage}%")
if current_power_off_battery_percentage == 20:
    print("Success")
time.sleep(2)
print(f"Setting power off percentage to 10%")
spc.write_power_off_percentage(10)
time.sleep(2) # Wait for the power off percentage to be updated
current_power_off_battery_percentage = spc.read_power_off_percentage()
print(f"Power off percentage: {current_power_off_battery_percentage}%")
if current_power_off_battery_percentage == 10:
    print("Success")
    
time.sleep(2)
print(f"Setting power off percentage to 0%")
spc.write_power_off_percentage(0)
time.sleep(2) # Wait for the power off percentage to be updated
current_power_off_battery_percentage = spc.read_power_off_percentage()
print(f"Power off percentage: {current_power_off_battery_percentage}%")
if current_power_off_battery_percentage == 0:
    print("Success")
else:
    print("Failed, power off percentage minimal is 5%")
