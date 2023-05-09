#!/usr/bin/python3
for i in range(122, 96):
    print("{:c}".format(str(i) if i % 2 == 0 else str(i + 65 - 97)), end="")
