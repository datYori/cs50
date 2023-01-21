#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Uggly way of implementing a mario pyramid """
def main():
    """ One function to rule them all """
    # init list of size 7 spaces char and 1 hash char at the end
    _n = 8
    leftside = [' ']*_n + ['#']
    for i in range(_n):
        leftside[_n-i] = '#'
        # reverse list without modifiying original list
        rightside = leftside[::-1]
        # change before last element into hash char
        print(''.join(leftside) + '  ' + ''.join(rightside))


if __name__ == '__main__':
    main()
