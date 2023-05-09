#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) + 65 - 97)
            new_str += ch
        else:
            new_str += ch
    print("{:s}".format(new_str))
