#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    print("{:d} {:s}{}".format(length, "argument" if length == 1 else "arguments", "." if length == 0 else ":"))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
