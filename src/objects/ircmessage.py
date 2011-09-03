#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time
from . import ircresponse

class InvalidIRCMessage(Exception): pass

class IRCMessage(ircresponse.IRCResponse):

    def __init__(self, message):

        super().__init__(message)

        self.messagify()


    def messagify(self):
        """The name's messagify simply because I felt like it. Deal with it."""

        if self.command != "privmsg":
            raise InvalidIRCMessage("not a PRIVMSG")

        if not self.message:
            raise InvalidIRCMessage("no message")

        self.target = self.args[0]


    @property
    def isMessage(self):
        return True

    def __str__(self):
        ret = [self.source, self.command, self.target, self.message]
        return str(ret)
