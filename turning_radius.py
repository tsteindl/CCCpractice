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


if steeringangle==0:
    print(0)
    print(dist)
    print(0)
else:
    alpha = (distToAngle(wheelbase, calcTurnRadius(wheelbase, steeringangle)))

    r = calcTurnRadius(wheelbase, steeringangle)
    y = r * math.sin(dist/r)
    s = r * math.cos(dist/r)
    x = r - s


    print(x)
    print(y)
    print(dist/circumference(calcTurnRadius(wheelbase, steeringangle)) * 360)


