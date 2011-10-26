#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse, ctcpmessage
from .. import irccommand

class PingListener(baselistener.BaseListener):

    def processLine(self, line):

        pingMsg = "{} PING from {}"


        if not line:
            return

        ret = ircresponse.IRCResponse(line)

        #Server pings

        if ret.command == "ping":
            source = ret.source

            ping_ = pingMsg.format(ret.cTimestamp, source)

            send = irccommand.IRCCommand("PONG", [], ret.source)

            # ~ self.master.log(ping_)
            self.master.sendCommand(send)

        #CTCP pings

        elif ret.canBeCTCPMessage:
            ret = ctcpmessage.CTCPMessage(line)
            target = ret.args[0]


            if not target.startswith("#") and ret.ctcpCommand == "ping":

                send = irccommand.IRCCommand("NOTICE", [ret.source], ret.rawMessage)
                self.master.sendCommand(send)


