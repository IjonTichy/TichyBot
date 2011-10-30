#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
from functions import maxspaces
import os

class MessageFortune(messagecommand.MessageCommand):

    TRIGGER = "!tb fortune"

    def respond(self, response):
        ret = " " * 513

        while len(ret) > 512:
            uptime = os.popen("fortune")
            ret = uptime.read()

            ret = ret.replace("\n\t", " ")
            ret = ret.replace("\n", " ")
            ret = ret.replace("\t", " ")
            ret = maxspaces.maxSpaces(ret)

        return ret
