#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os

from . import baselistener
from .. import ircresponse, ctcpmessage, irccommand

VERSIONDIR = os.path.abspath("../VERSION")

vFile = open(VERSIONDIR, "r")
version = vFile.read()
version = version.strip()
vFile.close()

class VersionListener(baselistener.BaseListener):

    def processLine(self, line):

        ctcp = "\x01VERSION {}\x01".format(version)

        ret = ircresponse.IRCResponse(line)

        if ret.canBeCTCPMessage:

            ret = ctcpmessage.CTCPMessage(line)

            target = ret.args[0]

            if not target.startswith("#"):   # assume it's directed to the bot

                if ret.ctcpCommand == "version":
                    send = irccommand.IRCCommand("NOTICE", [ret.source], ctcp)
                    self.master.sendCommand(send)
