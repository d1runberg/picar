#import qwiic package
import qwiic
import time
#capture a list of all supported qwiic boards on the i2c bus
results = qwiic.list_devices()

# print the listed results of the supported qwiic boards on the i2c bus, use to
# find your device on the bus.
#print(results)

# Select the ToF Distance sensor from the device list. You may need to change the
# array results depending on your list results.
ToF = qwiic.create_device(results[0][0])

#forever loop...
while True:
    try:
        #command the time of flight sensors to start ranging
        ToF.StartRanging()
        #give ToF sensor time to respond
        time.sleep(.005)
        #capture distance from the ToF sensor in mm
        distance = ToF.getDistance()
        #give ToF sensor time to respond
        time.sleep(.005)
        #command ToF sensor
        ToF.StopRanging()

        #print the distance to the console
        print("Distance(mm): %s" % distance)
        #wait half of a second
        time.sleep(.5)

    except Exception as e:
        #if error print error as e
        print(e)
