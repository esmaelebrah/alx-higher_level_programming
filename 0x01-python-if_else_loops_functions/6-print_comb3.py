#!/usr/bin/python3
for i in  range(0, 10):
    for j in range(i, 10):
        if i < j and  j == 9 and i >= 8:
            print(str(i) +str(j))
        elif j < i:
            print(str(j) + str(i), end=", ")
        elif i < j:
            print(str(i) + str(j), end=", ")
