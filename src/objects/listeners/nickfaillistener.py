#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os

from . import baselistener
from .. import ircresponse, irccommand

class NickFailListener(baselistener.BaseListener):

    def processLine(self, line):
        failmsg = "!!! Nickname is already in use."

        ret = ircresponse.IRCResponse(line)

        if ret.command == "433":

            self.master.log(failmsg)

            newName = ret.args[1] + "_"
            self.master.name = newName

            cmd = irccommand.IRCCommand("NICK", [newName], "")

            self.master.sendCommand(cmd)
