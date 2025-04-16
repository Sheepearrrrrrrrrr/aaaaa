from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Python = me sad
hub = PrimeHub()
lMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rMotor = Motor(Port.D)
handMotor = Motor(Port.A)
colorSensor = ColorSensor(Port.B)
base = DriveBase(lMotor, rMotor, 55.7, 129.8)
base.use_gyro(True)
yaw = hub.imu
base.settings(250)

dis = {
    Color.RED: (90, True),
    Color.YELLOW: (90, False),
    Color.WHITE: (-90, True),
    Color.GREEN: (-90, False)
}
# base.straight(100)
# for i in range(0, 16):
#     base.turn(90)
    # base.straight(100)
# base.curve(200, 90)
def main():
    print('started!')
    wait(500)
    yaw.reset_heading(0)
    base.settings(straight_speed=250)
    base.straight(350)
    turnByGyros(-90)
    base.straight(-300)
    base.straight(910)
    turnByGyros(-90)
    handMotor.run_target(650, -55)
    base.straight(80)
    for j in range(0, 3):
        handMotor.run_angle(650, 26)
        if (j != 2):
            base.straight(15)
    handMotor.run_angle(650, -45)
    base.straight(-120)
    turnByGyros(-90)
    handMotor.run_target(650, -55)
    base.straight(-300)
    base.straight(615)
    handMotor.run_angle(650, 20)
    turnByGyros(90)
    handMotor.run_target(650, -50)
    #blue water ball
    base.straight(100)
    handMotor.run_target(650, -35)
    base.straight(-100)
    #end
    #straigthen
    turnByGyros(90)
    base.straight(-500)
    #end
    #back to container
    base.straight(910)
    turnByGyros(-90)
    #end
    base.straight(120)
    handMotor.run_target(650, -60)
    handMotor.run_angle(650, 30)
    base.straight(-20)
    handMotor.run_angle(650, -30)
    turnByGyros(45)
    base.straight(40)
    handMotor.run_angle(650, 30)
    handMotor.run_angle(650, -30)
    base.straight(-40)
    turnByGyros(-45)
    base.straight(50)

def randomization():
    colors = []
    base.straight(190)
    for i in range(0, 6):
        colors.insert(0, colorSensor.color())
        base.straight(95.5)
        wait(100)
        print(colors)
    base.settings(450)
    base.turn(-45)
    base.straight(275)
    base.turn(-45)
    base.straight(-1100)
    base.straight(980)
    base.turn(-90)
    base.settings(250)
    for i in range(1, 4):
        currentBunch = i * 2 - 1
        base.straight(-200)
        base.straight(230)
        handMotor.run_target(250, -38)
        base.turn(-60)
        base.straight(75)
        handMotor.run_target(250, 0)
        base.straight(-75)
        base.turn(60)
        base.straight(-900)
        base.straight(500)
        base.turn(90)
        base.straight(100)
        index = 0
        for j in range(0, 2):
            shit = dis[]
            shit2 = currentBunch - j
            base.turn(shit[0])
            base.straight(100 if shit[1] else 50)
            base.turn(-shit[0])
            base.straight(100)
            break
        break
    
    
#main()
randomization()