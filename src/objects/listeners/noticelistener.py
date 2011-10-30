#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse, ircnotice, ctcpnotice
from functions import ansicodes, highestresponse

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

class NoticeListener(baselistener.BaseListener):

    def processLine(self, line):

        isCTCP   = False
        isAction = False

        channelMsgs =    (
        ("-",  SB + "{0}" + EB + ":" + SB + "{1}" + EB,  "-", " {2}"),
        ("-",  SB + "{0}" + EB + ":" + SB + "{1}" + EB,  "-", SB + "NOTICE:" + EB + " {2}"),
        ("-",  SB + "{0}" + EB,  "-",   " * " + SB + "{1}" + EB + " {2}"),
        )

        channelColors = (
        ("1", "-", "1", "-"),
        ("1", "-", "1", "-"),
        ("1", "-", "1", "-"),
        )

        serverChannelMsgs = (
        ("-", "N", "-", " {2}"),
        ("-", "N", "-", " {2}"),
        ("-", "N", "-", " *",  SB + " {1}" + EB + " {2}"),
        )

        serverChannelColors = (
        ("1", "E", "1", "-"),
        ("1", "B", "1", "-"),
        ("1", "B", "1", "D", "-"),
        )

        ret = highestresponse.highestResponse(line)

        if ret.isNotice:

            # Find message type
            if ret.isCTCPNotice:
                isCTCP = True

                if ret.ctcpCommand == "action":
                    isAction = True
                    endMsg   = ret.message
                else:
                    endMsg   = ret.fullMessage

            else:
                endMsg = ret.message

            srcSplit = ret.source.split(".")

            if len(srcSplit) > 1:
                src = srcSplit[-2]
            else:
                src = ret.source

            src2Split = self.master.server.split(".")

            if len(src2Split) > 1:
                src2 = src2Split[-2]
            else:
                src2 = self.master.server

            if src == src2:
                pMsg = serverChannelMsgs[isCTCP + isAction]
                pCol = serverChannelColors[isCTCP + isAction]
            else:
                pMsg = channelMsgs[isCTCP + isAction]
                pCol = channelColors[isCTCP + isAction]

            pMsg = ansicodes.mapColors(pMsg, pCol)

            self.master.log(pMsg.format(ret.target, ret.source, endMsg))



    def processAction(self, ircCommand, master):

        self.master = master
        line = ":{}!{}@dummy.address {}".format(self.master.name, self.master.uName,
                                                  str(ircCommand) )

        self.processLine(line)

