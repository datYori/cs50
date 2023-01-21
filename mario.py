#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pyramidLine(l, i):    # init list of size n-1 spaces char and 1 hash char at the end
    l[(len(l)-1)-i] = '#'
    oplist = l[::-1]
    return ''.join(l) + '  ' + ''.join(oplist)

def main(n):
    # init list of size n-1 spaces char and 1 hash char at the end
    list = [' ']*n + ['#']
    for i in range(n):
        print(pyramidLine(list, i))

if __name__ == '__main__':
    main(8)
