#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

class SelfNickListener(baselistener.BaseListener):

    def processLine(self, line):
        ret = ircresponse.IRCResponse(line)

        if ret.command == "nick":
            newNick = ret.args[0]

            if ret.source == self.master.name:
                self.master.name = newNick


