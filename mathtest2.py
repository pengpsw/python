#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand tamaype')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s