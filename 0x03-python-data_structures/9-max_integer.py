#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_mine = my_list.mine()
    list_mine.sort()
    return list_mine[-1]
