from flask import render_template
import qwiic

#define right and left motor
right = 0
left = 1

motors = qwiic.create_device(results[0][0])

if motors.begin()==True:
    print("Robot motor driver online, testing motors...")
    time.sleep(2)
else:
    print("motor Driver error!")

#enable motor driver functionality
motors.enable()

@app.route('/forward')
def forward():
    #drive both motors forward at full speed (255)
    motors.set_drive(left,1,255)
    motors.set_drive(right,1,255)
    #drive for 2 seconds
    time.sleep(2)
    motors.set_drive(left,1,0)
    motors.set_driver(right,1,0)
    return 'driving forward!'

@app.route('/reverse')
def reverse():
    #drive both motors forward at full speed (255)
    motors.set_drive(left,0,255)
    motors.set_drive(right,0,255)
    #drive for 2 seconds
    time.sleep(2)
    motors.set_drive(left,1,0)
    motors.set_driver(right,1,0)
    return 'driving reverse!'

###Create routes and responses for having the robot pivot left and right.


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
