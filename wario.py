#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # init list of size 7 spaces char and 1 hash char at the end
    n = 8
    list = [' ']*n + ['#']
    for i in range(n):
        list[n-i] = '#'
        # reverse list without modifiying original list
        oplist = list[::-1]
        # change before last element into hash char
        print(''.join(list) + '  ' + ''.join(oplist))


if __name__ == '__main__':
    main()
