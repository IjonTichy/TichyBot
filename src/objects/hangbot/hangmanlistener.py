#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..listeners import baselistener
from .. import ircresponse, ircmessage, ctcpmessage, irccommand

class HangmanListener(baselistener.BaseListener):

    def __init__(self):

        super().__init__()

        self.master = None
        self.channels = []

    def processLine(self, line):
        self.checkForMessage(line)
        self.checkJoin(line)
        self.checkPart(line)


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
            self.channels.append(ret.message)


    def checkPart(self, line):
        ret = ircresponse.IRCResponse(line)

        if ret.command == "part" and ret.source == self.master.name:
            target = ret.args[0]

            try:
                self.channels.remove(target)
            except ValueError:
                pass



    def processAction(self, ircCommand, master):

        self.master = master

        line = ":{}!{}@dummy.address {}".format(self.master.name, self.master.uName,
                                                  str(ircCommand) )

        self.processLine(line)

