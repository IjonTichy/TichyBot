#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..listeners import baselistener
from .. import ircresponse, ircmessage, ctcpmessage, irccommand

class ToChanListener(baselistener.BaseListener):

    def __init__(self):

        super().__init__()

        self.master = None
        self.channels = set()

    def processLine(self, line):
        self.checkForMessage(line)
        self.checkJoin(line)
        self.checkPart(line)
        self.checkKick(line)


    def checkForMessage(self, line):
        isCTCP   = False
        isAction = False
        tag      = "!tochan "

        ret = ircresponse.IRCResponse(line)

        if ret.canBeMessage:
            ret = ircmessage.IRCMessage(line)

            target = ret.args[0]

            # if CTCP message, ignore
            if ret.canBeCTCPMessage:
                return

            # ignore messages not directed to a monitored channel
            if target not in self.channels:
                return

            # ignore messages not starting with '!global'
            if not ret.message.startswith(tag):
                return

            msg = ret.message[len(tag):]
            msgList = msg.split()

            otherChan = msgList[0]
            mMsg = " ".join(msgList[1:])

            if otherChan in self.channels:

                sMsg = "from {}: {}".format(target, mMsg)

                send = irccommand.IRCCommand("NOTICE", [otherChan], sMsg)
                self.master.sendCommand(send)


    def checkJoin(self, line):
        ret = ircresponse.IRCResponse(line)

        if ret.command == "join" and ret.source == self.master.name:
            self.channels.add(ret.message)


    def checkPart(self, line):
        ret = ircresponse.IRCResponse(line)

        if ret.command == "part" and ret.source == self.master.name:
            target = ret.args[0]

            if target in self.channels:
                self.channels.remove(target)


    def checkKick(self, line):
        ret = ircresponse.IRCResponse(line)

        if ret.command == "kick":

            channel, kicked = ret.args[0:2]

            print(repr(kicked))

            if kicked == self.master.name:

                if channel in self.channels:
                    self.channels.remove(channel)




    def processAction(self, ircCommand, master):

        self.master = master

        line = ":{}!{}@dummy.address {}".format(self.master.name, self.master.uName,
                                                  str(ircCommand) )

        self.processLine(line)

