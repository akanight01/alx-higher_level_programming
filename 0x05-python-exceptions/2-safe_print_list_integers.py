#!/user/bin/python3
def afe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            c += 1
    print()
    return (c)
