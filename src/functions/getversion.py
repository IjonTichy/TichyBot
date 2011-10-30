#!/usr/bin/python3

# -*- coding: utf-8 -*-


def getVersion(path):
    vFile = open(path, "r")
    version = vFile.read()
    version = version.strip()
    vFile.close()

    return version
