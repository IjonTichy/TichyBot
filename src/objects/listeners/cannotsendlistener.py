#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class CannotSendListener(baselistener.BaseListener):

    def processLine(self, line):
        cannotSendMsg = "{} {}: {}"
        ret = ircresponse.IRCResponse(line)
        if ret.command == "404":
            self.master.log(cannotSendMsg.format(ret.cTimestamp, ret.source, ret.message))


