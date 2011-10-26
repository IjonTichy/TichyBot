#!/usr/bin/env python3

# -*- coding: utf-8 -*-



class BaseListener(object):

    def __init__(self):
        self.master = None
        pass


    def process(self, message, master):
        self.master = master

        if not message:
            return

        ret = []

        for line in message.split("\n"):

            response = self.processLine(line)

            if response:
                ret.append(response)

        return "\n".join(ret)

    def processAction(self, command, master):
        pass

    def processLine(self, message):
        raise RuntimeError("processLine should not be run with {}".format(self.__class__.__name__) )
