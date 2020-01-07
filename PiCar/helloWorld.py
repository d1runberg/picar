#import qwiic module
import qwiic

#capture a list of all supported qwiic boards on the i2c bus
results = qwiic.list_devices()

#print the listed results of the supported qwiic boards on the i2c bus
print(results)

# Select a device from the list and creat an instance of it
mydevice = qwiic.create_device(results[0][0])

#print out the specific device
print(mydevice)
