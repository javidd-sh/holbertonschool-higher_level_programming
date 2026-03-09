#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1  # exclude the script name

    if argc == 0:
        print("0 arguments.")
    else:
        word = "argument" if argc == 1 else "arguments"
        print("{} {}:".format(argc, word))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
