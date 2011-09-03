#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class KickListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} {} [{}] has kicked {} from {} ({})"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "kick":

            self.master.log(leaveMsg.format(ret.cTimestamp, source, sourceHost, kicked, channel, reason))
