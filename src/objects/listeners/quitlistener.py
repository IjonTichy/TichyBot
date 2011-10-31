#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

class QuitListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = ("{} ", "[", "{}", "]", " has quit ", "(", "{}", ")")
        leaveCol = ("6", "A", "6", "A", "-", "A", "-", "A")

        ret = ircresponse.IRCResponse(line)

        if ret.command == "quit":

            msg = ansicodes.mapColors(leaveMsg, leaveCol)

            self.master.log(msg.format(ret.source, ret.sourceFull, ret.message) )
