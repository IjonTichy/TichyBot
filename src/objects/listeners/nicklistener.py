#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class NickListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} is now known as {}"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "nick":
            newNick = ret.args[0]
            self.master.log(leaveMsg.format(ret.cTimestamp, ret.source, newNick) )

            if ret.source == self.master.name:
                self.master.name = newNick


