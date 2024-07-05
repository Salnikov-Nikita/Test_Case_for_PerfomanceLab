import sys
n = int(sys.argv[1])
m = int(sys.argv[2])

k = 0
while True:
    print(k + 1, end = '')
    k = (k + (m - 1)) % n
    if k == 0:
        break