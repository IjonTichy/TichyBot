#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse, ircmessage, ctcpmessage

class MessageListener(baselistener.BaseListener):

    def processLine(self, line):

        isCTCP   = False
        isAction = False
        channelMsg = ("[{}]<{}> {}", "[{}]<(ctcp){}> {}", "[{}] * {} {}")

        if not line:
            return

        ret = ircresponse.IRCResponse(line)

        if ret.canBeMessage:
            ret = ircmessage.IRCMessage(line)

            # Find message type
            if ret.canBeCTCPMessage:
                isCTCP = True
                ret = ctcpmessage.CTCPMessage(line)

                if ret.ctcpCommand == "action":
                    isAction = True
                    endMsg   = ret.message
                else:
                    endMsg   = ret.fullMessage

            else:
                endMsg = ret.message


            pMsg = "{} " + channelMsg[isCTCP + isAction]
            self.master.log(pMsg.format(ret.cTimestamp, ret.target, ret.source, endMsg))
