#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def join(split_command):
    ret = ''
    for i, c in enumerate(split_command):
        if (' ' in c) == True: 
            ret = ''.join([ret, '\''])
            ret = ''.join([ret, c])
            ret = ''.join([ret, '\''])
        else: 
            ret = ''.join([ret, c])

        if i != (len(split_command) - 1):
            ret = ''.join([ret, ' '])

    return ret


