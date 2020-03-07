#!/usr/bin/env python

from lib.Bakery import *
import sys

if __name__ == '__main__':

    bakery = Bakery()
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        with open(input_file, 'r') as order_file:
            text = order_file.read()
        bakery = Bakery()
        bakery.place_order(text)
    else:
        lines = []
        print("Place order:")
        while True:
            line = raw_input()
            if line:
                lines.append(line)
            else:
                break
        text = '\n'.join(lines)
        bakery.place_order(text)
