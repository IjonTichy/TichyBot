#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

class MOTDListener(baselistener.BaseListener):

    def processLine(self, line):

        motdMsg = ("-", "M", "-", " {}")
        motdCol = ("1", "D", "1", "-")

        smotdMsg = ("-", "M", "-", " {}")
        smotdCol = ("1", "C", "1", "-")

        emotdMsg = ("-", "M", "-", " {}")
        emotdCol = ("1", "B", "1", "-")

        isofmotd = False

        ret = ircresponse.IRCResponse(line)

        if ret.command == "372":   # MOTD
            isofmotd = True
            msg = motdMsg
            col = motdCol

        elif ret.command == "375": # start MOTD
            isofmotd = True
            msg = smotdMsg
            col = smotdCol


        elif ret.command == "376": # end MOTD
            isofmotd = True
            msg = emotdMsg
            col = emotdCol

        if isofmotd:
            retmsg = ansicodes.mapColors(msg, col)

            self.master.log(retmsg.format(ret.message))
