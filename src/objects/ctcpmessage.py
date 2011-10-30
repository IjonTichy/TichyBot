#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time
from . import ircmessage

class InvalidCTCPMessage(Exception): pass

class CTCPMessage(ircmessage.IRCMessage):

    def __init__(self, message):

        super().__init__(message)

        self.ctcpify()


    def ctcpify(self):
        """Special initialisation for CTCPMessage
Again, I felt like giving it this stupid name. DEAL WIT IT"""

        if not (self.message.startswith("\x01") and self.message.endswith("\x01")):
            raise InvalidCTCPMessage("not a CTCP message")

        oldMessage       = self.message

        self.rawMessage  = oldMessage
        self.fullMessage = self.rawMessage[1:-1]

        msgPart          = self.fullMessage.partition(" ")

        self.ctcpCommand = msgPart[0].lower()
        self.message     = msgPart[2]


    @property
    def isCTCPMessage(self):
        return True
