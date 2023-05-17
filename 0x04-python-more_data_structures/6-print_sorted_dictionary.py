#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = [k for k, v in a_dictionary.items()]
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
