#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener

class EchoListener(baselistener.BaseListener):

    def processLine(self, line):
        if line:
            print(line)

