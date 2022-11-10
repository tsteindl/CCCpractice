from util import drive_segment

input = input()
dists = []
steering_angles = []
wheelbase = 0.0

def parse_input(string):
    arr = string.split(" ")
    wheelbase = float(arr[0])
    n = int(arr[1])
    for i in range(n):
        dists.append(float(arr[2 + i*2]))
        steering_angles.append(float(arr[2 + i*2 + 1]))
    return wheelbase

wheelbase = parse_input(input)

x_0 = 0.0
y_0 = 0.0
dir = 0.0
for dist, sa in zip(dists, steering_angles):
    (new_x, new_y, new_dir) = drive_segment(wheelbase, dist, sa)
    x_0 + new_x
    y_0 + new_y
    dir + new_dir


print(f"{x_0} {y_0} {dir}")