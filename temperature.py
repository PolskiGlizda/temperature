#! /usr/bin/python

import sys
import argparse

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    temp = args[1]
    if args[1] == "--help":
        help()
    if args[1] == "-h":
        help()
    if args[1] == "-f":
        ctof(temp)
    if args[1] == "-c":
        ftoc(temp)


def help():
    print("Usage: temperature [OPTION] number\n Options: \n -f from celsius to farenheit \n -c from farenheit to celsius")
def ctof(temp):
    return (1.8 * temp) + 32
def ftoc(temp):
    return (temp + 32)/1.8

if __name__ == "__name__":
    main()
