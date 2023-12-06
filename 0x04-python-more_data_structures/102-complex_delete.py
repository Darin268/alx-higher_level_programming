#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] is value:
            del a_dictionary[k]
    return a_dictionary
