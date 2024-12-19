#!/usr/bin/python3
""" find the maximum number in a list """
def max_integer(my_list=[]):
    if my_list:
        max_num = my_list[0]
        for num in my_list:
            if num > max_num:
                max_num = num
        return max_num
    else:
        return None
