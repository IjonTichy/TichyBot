#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

# :ijontichy!~ijontichy@powernoob KICK #testbotcrap ijon :

class KickListener(baselistener.BaseListener):

    def processLine(self, line):

        leaveMsg = "{} [{}] has kicked {} from {} ({})"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "kick":

            channel, kicked = ret.args[0:2]

            self.master.log(leaveMsg.format(ret.source, ret.sourceFull, kicked, channel, ret.message))
