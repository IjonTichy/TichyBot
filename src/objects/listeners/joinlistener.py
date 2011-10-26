#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

class JoinListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = ("{}", " [", "{}", "]", " has joined " + SB + "{}" + EB)
        leaveCol = ("G", "A", "6", "A", "-")

        ret = ircresponse.IRCResponse(line)

        if ret.command == "join":

            msg = ansicodes.mapColors(leaveMsg, leaveCol)

            self.master.log(msg.format(ret.source, ret.sourceFull, ret.message))


