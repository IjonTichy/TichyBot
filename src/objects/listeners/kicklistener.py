#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

# :ijontichy!~ijontichy@powernoob KICK #testbotcrap ijon :

class KickListener(baselistener.BaseListener):

    def processLine(self, line):

        kickMsg = ("{}", " has kicked " + SB + "{}" + EB + " from " + SB + "{}" + EB, " (", "{}", ")")
        kickCol = ("6",  "-", "A", "-",  "A")
        ret = ircresponse.IRCResponse(line)

        if ret.command == "kick":

            channel, kicked = ret.args[0:2]

            msg = ansicodes.mapColors(kickMsg, kickCol)

            self.master.log(msg.format(ret.source, kicked, channel, ret.message))
