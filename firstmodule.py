#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Bill Xie'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world')
    elif len(args) == 2:
        print('Hello, {0}!'.format(args[1]))
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'This is my name, %s' % name

def __private2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return __private2(name)

if __name__ == '__main__':
    test()