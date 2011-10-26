#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import copy

class MessageStorer(object):

    def __init__(self):

        self.lines = []

    def addLine(self, line):
        self.lines.append(line)

    def tail(self, count):
        return self.lines[-count:]

    def head(self, count):
        return self.lines[:count]


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, other):
        assert isinstance(other, list), "lines must be list, not {}".format(other.__class__.__name)
        self.__lines = other


