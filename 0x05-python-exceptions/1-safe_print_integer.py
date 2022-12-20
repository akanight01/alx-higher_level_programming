#!/user/bin/python3
def afe_print_integer(value):
    try:
        int(value)
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
