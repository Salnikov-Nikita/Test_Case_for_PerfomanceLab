import sys

file = open(sys.argv[1])
x_o, y_o = map(float, file.readline().split())

r = float(file.readline())

for line in open(sys.argv[2]):
    x, y = map(float, line.split())
    test = (x_o - x) ** 2 + (y_o - y) ** 2 - r ** 2
    if test == 0:
        print(0)
    elif test > 0:
        print(2)
    else:
        print(1)
