import math

def degToRad(deg):
    return deg/180*math.pi


def calcTurnRadius(wheelbase, steeringangle):
    return wheelbase / math.sin(degToRad(steeringangle))


def circumference(radius):
    return 2*radius*math.pi


def distToAngle(wheelbase, radius):
    return math.asin(wheelbase/radius)


def drive_segment(wheelbase, dist, steering_angle):
    if steering_angle == 0:
        return (0, dist, 0)
    else:
        #alpha = (distToAngle(wheelbase, calcTurnRadius(wheelbase, steering_angle)))

        r = calcTurnRadius(wheelbase, steering_angle)
        y = r * math.sin(dist / r)
        s = r * math.cos(dist / r)
        x = r - s

        newDir = dist / circumference(calcTurnRadius(wheelbase, steering_angle)) * 360 % 360

        return x, y, newDir
        #printValues(x, y, newDir)