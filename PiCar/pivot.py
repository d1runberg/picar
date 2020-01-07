#import qwiic module
import qwiic
import time
#capture a list of all supported qwiic boards on the i2c bus
#results = qwiic.list_devices()

#print the listed results of the supported qwiic boards on the i2c bus
#print(results)

#define right and left motor
right = 0
left = 1

# Select a device from the list and creat an instance of it
motors = qwiic.create_device(results[0][0])

if motors.begin()==True:
    print("Robot motor driver online, testing motors...")
    time.sleep(2)
else:
    print("motor Driver error!")

#enable motor driver functionality
motors.enable()
#drive both motors forward at full speed (255)
motors.set_drive(left,1,255)
motors.set_drive(right,0,255)
#drive for 2 seconds
time.sleep(2)
#set motor speed to stop (0) for both motors
motors.set_drive(left,0,255)
motors.set_driver(right,1,255)
#drive for 2 seconds
time.sleep(2)
#stop both motors
motors.set_drive(left,1,0)
motors.set_driver(right,1,0)
#robot pivot in alternate direction
#disable motor driver functionality
motors.disable()
