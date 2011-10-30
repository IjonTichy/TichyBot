#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

class NickListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = ("{}", " is now known as ", "{}")
        leaveCol = ("6",  "-",                 "G")

        ret = ircresponse.IRCResponse(line)

        if ret.command == "nick":
            newNick = ret.args[0]

            msg = ansicodes.mapColors(leaveMsg, leaveCol)

            self.master.log(msg.format(ret.source, newNick) )

            if ret.source == self.master.name:
                self.master.name = newNick


