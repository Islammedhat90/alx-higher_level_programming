#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv)
    sum = 0

    if arg_len == 1:
        sum = 0
    else:
        for index in range(1, arg_len):
            sum += int(argv[index])

    print("{:d}".format(sum))
