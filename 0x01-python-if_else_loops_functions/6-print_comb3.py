#!/usr/bin/python3
for x in  range(0, 10):
    for y in range(x, 10):
        if x < y:
            print(str(x) +str(y), end=", ")
        elif y < x:
            print(str(y) + str(x), end=", ")
        elif y == 9:
            print(str(x) + str(y))
