#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" A more clean way of implementing a mario pyramid """
def pyramid_line(leftside, _i):
    """ A more clean way of implementing a mario pyramid """
    # change last space in hash
    leftside[(len(leftside)-1)-_i] = '#'
    # reverse list without modifiying original list
    rightside = leftside[::-1]
    return ''.join(leftside) + '  ' + ''.join(rightside)

def main(_n):
    """ A more clean way of implementing a mario pyramid """
    # init list of size n spaces char and 1 hash char at the end
    initline = [' ']*_n + ['#']
    for i in range(_n):
        print(pyramid_line(initline, i))

if __name__ == '__main__':
    main(8)
