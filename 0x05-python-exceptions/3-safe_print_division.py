#!/usr/bin/python3
def afe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
