import math


wheelbase = float(input('Wheelbase:'))
dist = float(input('Distance:'))
steeringangle = float(input('Steeringangle:'))


def degToRad(deg):
    return deg/180*math.pi


def calcTurnRadius(wheelbase, steeringangle):
    return round(wheelbase / math.sin(degToRad(steeringangle)), 3)


def circumference(radius):
    return 2*radius*math.pi


def distToAngle(wheelbase, radius):
    return math.asin(wheelbase/radius)


alpha = (distToAngle(wheelbase, calcTurnRadius(wheelbase, steeringangle)))

r = calcTurnRadius(wheelbase, steeringangle)
y = r * math.sin(dist/r)
s = r * math.cos(dist/r)
x = r - s


print(x)
print(y)
print(dist/circumference(calcTurnRadius(wheelbase, steeringangle)) * 360)


