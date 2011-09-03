#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class QuitListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} [{}] has quit ({})"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "quit":

            self.master.log(leaveMsg.format(ret.cTimestamp, ret.source, ret.sourceFull,
                                            ret.message) )
