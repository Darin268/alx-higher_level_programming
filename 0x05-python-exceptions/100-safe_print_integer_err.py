#!/usr/bin/python3
import sys



def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as v:
        print('Exception:', v, file=sys.stderr)
        return False
    except TypeError as t:
        print('Exception:', t, file=sys.stderr)
        return False
