from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Port, Direction
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
base.settings(350)
stopwatch = StopWatch()

dis = {
    Color.RED: (90, True),
    Color.YELLOW: (90, False),
    Color.WHITE: (-90, False),
    Color.GREEN: (-90, True)
}

def randomization():
    base.straight(300)
    base.turn(-90)
    base.straight(420)
    base.turn(90)
    base.straight(120)
    rHandMotor.run_target(400, -15)
    base.turn(10)
    base.straight(-50)
    base.straight(90)
    rHandMotor.run_target(400, -175)
    base.straight(-100)
    base.turn(-10)
    base.straight(-150)
    base.turn(-90)
    base.straight(350)
    base.turn(90)
    base.straight(745)
    base.turn(90)
    base.straight(-100)
    colors = []
    base.straight(190)
    for i in range(0, 6):
        color = colorSensor.color()
        colors.insert(0, color)
        base.straight(95.5)
        print(colors)
        hub.light.on(color)
        wait(100)
    base.turn(-45)
    base.straight(225)
    base.turn(-45)
    base.straight(-1075)
    base.straight(1000)
    base.turn(-90)
    for i in range(1, 4):
        currentBunch = i * 2 - 1
        if colors[currentBunch] == Color.NONE and colors[currentBunch - 1] == Color.NONE:
            continue
        base.straight(i * -400)
        
        to_turn = 40
        base.straight(i * 175)
        if colors[currentBunch] != Color.NONE:
            rHandMotor.run_target(400, -4, wait=False)
        lHandMotor.run_target(400, -4)
        base.turn(-40)
        base.straight(125)
        lHandMotor.run_target(400, -65)
        base.straight(-70)
        if colors[currentBunch] != Color.NONE:
            base.curve(144, -30)
            base.straight(100)
            rHandMotor.run_target(400, -65)
            base.straight(-200)
            to_turn = 70
        base.turn(to_turn)
        base.straight(-400 - i * 100)

        base.straight(525)
        base.turn(90)
        base.straight(175)
        for j in range(0, 2):
            shit2 = currentBunch - j
            if colors[shit2] == Color.NONE:
                continue
            shit = dis[colors[shit2]]
            base.turn(shit[0])
            base.straight(350)
            base.turn(-shit[0])
            base.straight(575)
            if j == 0:
                base.turn(0 if shit[1] else -65)
                rHandMotor.run_target(400, -4)
                base.straight(-100)
                rHandMotor.run_target(400, -175)
                base.straight(100)
                base.turn(0 if shit[1] else 65)
            else:
                base.turn(-15 if not shit[1] else 65)
                lHandMotor.run_target(400, -4)
                base.straight(-100)
                lHandMotor.run_target(400, -175)
                base.straight(100)
                base.turn(15 if not shit[1] else -65)
            base.straight(-550)
            base.turn(-shit[0])
            base.straight(375)
            base.turn(shit[0])
        if i <= 2:
            base.straight(-175)
            base.turn(-90)
    base.settings(650)
    base.straight(1200)
    base.straight(-200)
    print(stopwatch.time())

randomization()
