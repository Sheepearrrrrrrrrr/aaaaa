from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
lMotor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
rMotor = Motor(Port.E)
rHandMotor = Motor(Port.A)
lHandMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
colorSensor = ColorSensor(Port.C)
base = DriveBase(lMotor, rMotor, 55.7, 144)
base.use_gyro(True)
yaw = hub.imu
base.settings(350)

dis = {
    Color.RED: (90, 420),
    Color.YELLOW: (90, 310),
    Color.WHITE: (-90, 450),
    Color.GREEN: (-90, 340)
}

def randomization():
    base.straight(300)
    base.turn(-90)
    base.straight(420)
    base.turn(90)
    base.straight(125)
    rHandMotor.run_target(400, -18)
    base.turn(10)
    base.straight(40)
    base.straight(-50)
    rHandMotor.run_target(400, -176)
    base.turn(-10)
    base.straight(-150)
    base.turn(-90)
    base.straight(350)
    base.turn(90)
    base.straight(705)
    base.turn(90)
    base.straight(-100)
    colors = []
    base.straight(190)
    for i in range(0, 6):
        colors.insert(0, colorSensor.color())
        base.straight(95.5)
        wait(100)
        print(colors)
    base.settings(400)
    base.turn(-45)
    base.straight(225)
    base.turn(-45)
    base.straight(-1075)
    base.straight(960)
    base.turn(-90)
    base.settings(350)
    for i in range(1, 4):
        #print('starting a bunch')
        currentBunch = i * 2 - 1
        if colors[currentBunch] == Color.NONE and colors[currentBunch - 1] == Color.NONE:
            continue
        # base.straight(-200)
        # base.straight(180 + i * 50)
        '''
            Arm stuff
        '''
        base.straight(-400 - i * 100)
        base.straight(525)
        base.turn(90)
        base.straight(175)
        index = 0
        for j in range(0, 2):
            shit2 = currentBunch - j
            if colors[shit2] == Color.NONE:
                continue
            shit = dis[colors[shit2]]
            base.turn(shit[0])
            base.straight(shit[1])
            base.turn(-shit[0])
            base.straight(500)
            '''
            Arm stuff
            '''
            base.straight(-500)
            base.turn(-shit[0])
            base.straight(shit[1])
            base.turn(shit[0])
        if i <= 2:
            base.straight(-175)
            base.turn(-90)
    base.straight(700)
    #print('Probably ended')

randomization()
