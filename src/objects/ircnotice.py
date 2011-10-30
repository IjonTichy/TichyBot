#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time
from . import ircresponse

class InvalidIRCNotice(Exception): pass

class IRCNotice(ircresponse.IRCResponse):

    def __init__(self, message):

        super().__init__(message)

        self.noticeify()


    def noticeify(self):
        """Special initialisation for IRCNotice
These names are now a running gag."""

        if self.command != "notice":
            raise InvalidIRCNotice("not a PRIVMSG")

        if not self.message:
            raise InvalidIRCNotice("no message")

        self.target = self.args[0]


    @property
    def isNotice(self):
        return True

    def __str__(self):
        ret = [self.source, self.command, self.target, self.message]
        return str(ret)
