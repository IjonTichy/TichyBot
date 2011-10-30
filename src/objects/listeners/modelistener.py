#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

class ModeListener(baselistener.BaseListener):

    def processLine(self, line):

        modeMsg = ("mode/", "{} ", "[", "{}", "]", " by " + SB + "{}" + EB)
        modeCol = ("-",     "6",   "A", "-",  "A", "-")

        myModeMsg = ("mode/", "{} ", "[", "{}", "]")
        myModeCol = ("-",     "6",   "A", "-",  "A")

        ret = ircresponse.IRCResponse(line)

        if ret.command == "mode":

            setter = ret.source
            recip  = ret.args[0]
            args   = ret.args[1:]

            if setter == recip:
                msg = ansicodes.mapColors(myModeMsg, myModeCol)
            else:
                msg = ansicodes.mapColors(modeMsg, modeCol)

            self.master.log(msg.format(recip, " ".join(args), setter) )


