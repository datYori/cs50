#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Uggly way of implementing a mario pyramid """
def main():
    """ One function to rule them all """
    # init
    _n = 8
    leftside = [' ']*_n + ['#']
    for i in range(_n):
        leftside[_n-i] = '#'
        # reverse list without modifiying original list
        rightside = leftside[::-1]
        print(''.join(leftside) + '  ' + ''.join(rightside))

if __name__ == '__main__':
    main()
