#!/usr/bin/python3

# -*- coding: utf-8 -*-


def getInfo(path):
    iFile = open(path, "r")
    info = iFile.read()
    info = info.replace("\n", " ")
    info = info.strip()
    iFile.close()

    return info
