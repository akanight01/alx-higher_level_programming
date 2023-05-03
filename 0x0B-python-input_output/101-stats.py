#!/usr/bin/python3
<<<<<<< HEAD
=======
<<<<<<< HEAD
import sys


def print_info():
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0
file_size = 0

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except:
            pass

        try:
            file_size += int(pieces[-1])
        except:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
=======
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
<<<<<<< HEAD
=======
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
