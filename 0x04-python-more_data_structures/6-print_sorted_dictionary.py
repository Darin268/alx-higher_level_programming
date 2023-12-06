#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for y in sorted(a_dictionary.keys()):
        print("{}: {}".format(y, a_dictionary[y]))
