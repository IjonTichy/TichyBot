#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time
from . import ircnotice

class InvalidCTCPNotice(Exception): pass

class CTCPNotice(ircnotice.IRCNotice):

    def __init__(self, message):

        super().__init__(message)

        self.ctcpify()


    def ctcpify(self):


        if not (self.message.startswith("\x01") and self.message.endswith("\x01")):
            raise InvalidCTCPNotice("not a CTCP notice")

        oldMessage       = self.message

        self.rawMessage  = oldMessage
        self.fullMessage = self.rawMessage[1:-1]

        msgPart          = self.fullMessage.partition(" ")

        self.ctcpCommand = msgPart[0].lower()
        self.message     = msgPart[2]


    @property
    def isCTCPNotice(self):
        return True
