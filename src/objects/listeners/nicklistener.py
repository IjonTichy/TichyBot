#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class NickListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} is now known as {}"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "nick":

            self.master.log(leaveMsg.format(ret.cTimestamp, ret.source, ret.args[0]) )
