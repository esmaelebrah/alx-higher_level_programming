#!/usr/bin/python3
def weight_average(my_list=[]):
    product = 0
    sum = 0
    for i in range(len(my_list)):
        product += (my_list[i][0] * my_list[i][1])
        sum += my_list[i][1]
    return (product / sum) if sum else 0
