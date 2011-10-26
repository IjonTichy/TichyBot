#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..objects import ircresponse, ircmessage, ctcpmessage, ctcpnotice

def highestResponse(response):
    ret = ircresponse.IRCResponse(line)

    if ret.canBeMessage:
        ret = ircmessage.IRCMessage(line)

        if ret.canBeCTCPMessage:
            ret = ctcpmessage.CTCPMessage(line)

    elif ret.canBeNotice:
        ret = ircnotice.IRCNotice(line)

        if ret.canBeCTCPNotice:
            ret = ctcpnotice.CTCPNotice(line)

    return ret
