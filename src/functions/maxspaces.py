#!/usr/bin/python3

# -*- coding: utf-8 -*-

def maxSpaces(line, spaceMax=5):
    spaces = 0
    ret = []

    for char in line:
        if char == " ":
            if spaces >= spaceMax:
                continue
            else:
                spaces += 1
        else:
            spaces = 0
        ret.append(char)

    return "".join(ret)
