#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

class PartListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = ("{}", " [", "{}", "]", " has left " + SB + "{}" + EB, " (", "{}", ")")
        leaveCol = ("G", "A", "6", "A", "-", "A", "-", "A")

        ret = ircresponse.IRCResponse(line)

        if ret.command == "part":

            target = ret.args[0]

            msg = ansicodes.mapColors(leaveMsg, leaveCol)

            self.master.log(msg.format(ret.source, ret.sourceFull, target, ret.message))


