#!/usr/bin/python3
def number_keys(a_dictionary):
    numOfKey = 0
    for k, v in a_dictionary.items():
        numOfKey += 1
    return numOfKey
