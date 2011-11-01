#!/usr/bin/python3

# -*- coding: utf-8 -*-


def getUsers(path):
    uFile = open(path, "r")
    usersRaw = uFile.read().strip()

    users = set(usersRaw.split())

    uFile.close()

    return users
