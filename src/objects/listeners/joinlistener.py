#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class JoinListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} [{}] has joined {}"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "join":

            self.master.log(leaveMsg.format(ret.cTimestamp, ret.source, ret.sourceFull, ret.message))


