import math


wheelbase = float(input('Wheelbase:'))
dist = float(input('Distance:'))
steeringangle = float(input('Steeringangle:'))


def degToRad(deg):
    return deg/180*math.pi


def calcTurnRadius(wheelbase, steeringangle):
    return wheelbase / math.sin(degToRad(steeringangle))


def circumference(radius):
    return 2*radius*math.pi


def distToAngle(wheelbase, radius):
    return math.asin(wheelbase/radius)


def printTurnRadius(wheelbase, steeringAngle):
    print(round(calcTurnRadius(wheelbase, steeringangle), 2))

def printValues(x, y, newDir):
    print(round(x, 2), round(y, 2), round(newDir, 2))


print("TurnRadius: ")
printTurnRadius(wheelbase, steeringangle)
print("Level2")




drive_segment()

