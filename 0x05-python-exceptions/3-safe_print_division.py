#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (FloatingPointError, ZeroDivisionError):
        result = None
    finally:
        print("The main result	is : {}".format(result))

    return result
