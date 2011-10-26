#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..listeners import baselistener
from .. import ircresponse, ircmessage, ctcpmessage, irccommand
from . import storechanobj

class StoreChanListener(baselistener.BaseListener):

    def __init__(self):

        super().__init__()

        self.master = None
        self.channelObjs = {}

    def add(self, channel):
        newObj = storechanobj.MessageStorer()
        self.channelObjs[channel] = newObj

    def remove(self, channel):
        if channel in self.channelObjs:
            del self.channelObjs[channel]


    def processLine(self, line):

        ret = ircresponse.IRCResponse(line)

        self.checkForMessage(ret)
        self.checkJoin(ret)
        self.checkPart(ret)
        self.checkKick(ret)


    def checkForMessage(self, line):
        isCTCP   = False
        isAction = False
        tag = "!store "


        if line.canBeMessage:
            ret = ircmessage.IRCMessage(line.response)

            # if CTCP message, ignore
            if ret.canBeCTCPMessage:
                return

            # ignore messages not directed to a monitored channel
            if ret.target not in self.channelObjs:
                return

            if not line.message.startswith(tag):
                return
            else:
                ret.message = ret.message[len(tag):]

            self.checkAddLine(ret)
            self.checkPrintLines(ret)


    def checkAddLine(self, line):
        tag = "add "

        if not line.message.startswith(tag):
            return

        msg = line.message[len(tag):]

        self.channelObjs[line.target].addLine(msg)


    def checkPrintLines(self, line):
        tag = "print"

        if line.message != tag:
            return

        for i in self.channelObjs[line.target].tail(5):
            send = irccommand.IRCCommand("NOTICE", [line.target], i)
            self.master.sendCommand(send)


    def checkJoin(self, line):

        if line.command == "join" and line.source == self.master.name:
            self.add(line.message)


    def checkPart(self, line):

        if line.command == "part" and line.source == self.master.name:
            target = line.args[0]
            self.remove(target)


    def checkKick(self, line):

        if line.command == "kick":

            channel, kicked = line.args[0:2]

            if kicked == self.master.name:
                self.remove(channel)




    def processAction(self, ircCommand, master):
        self.master = master

        line = ":{}!{}@dummy.address {}".format(self.master.name, self.master.uName,
                                                  str(ircCommand) )

        self.processLine(line)
