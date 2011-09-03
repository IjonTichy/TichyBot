#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class PartListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} [{}] has left {} ({})"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "part":

            target = ret.args[0]

            self.master.log(leaveMsg.format(ret.cTimestamp, ret.source,
                                            ret.sourceFull, target, ret.message))


