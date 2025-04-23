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
    Color.RED: (90, 100),
    Color.YELLOW: (90, 50),
    Color.WHITE: (-90, 100),
    Color.GREEN: (-90, 50)
}

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
        print('starting a bunch')
        currentBunch = i * 2 - 1
        if colors[currentBunch] == Color.NONE && colors[currentBunch - 1] == Color.NONE:
            continue
        base.straight(-200)
        base.straight(180 + i * 50)
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
            shit2 = currentBunch - j
            if colors[shit2] == Color.NONE:
                continue
            shit = dis[shit2]
            base.turn(shit[0])
            base.straight(shit[1])
            base.turn(-shit[0])
            base.straight(100)
            '''
            Arm stuff
            '''
            base.straight(-100)
            base.turn(-shit[0])
            base.straight(shit[1])
            base.turn(shit[0])
        if i <= 2:
            base.straight(-100)
            base.turn(-90)
            base.straight(-350)
    base.straight(500)
    print('Probably ended')

randomization()
