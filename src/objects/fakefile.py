#!/usr/bin/env python3

# -*- coding: utf-8 -*-

class FakeFile(object):

    def __init__(self):
        self.data = ""

    def read(self, size=None):
        if size is None:
            return self.data
        else:
            return self.data[:size]

    def write(self, wData):
        self.data += wData

        return len(wData)
