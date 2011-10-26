#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time

class InvalidIRCResponse(Exception): pass

class IRCResponse(object):

    def __init__(self, message):

        self.cTime      = time.gmtime()
        self.cTimestamp = time.strftime("<%H:%M>", self.cTime)

        self.response = message
        self.parseCommand()



    def parseCommand(self):

        source     = ""
        sourceFull = ""
        sourceHost = ""
        sourceUser = ""
        command    = ""
        args       = ""
        message    = ""

        msg = self.response.lstrip(":")
        msgList = msg.partition(":")

        if self.response:

            if not self.response.startswith(":"):

                if msg.startswith("PING"):

                    source     = msgList[2]
                    sourceFull = msgList[2]
                    sourceHost = msgList[2]
                    sourceUser = msgList[2]

                    command = msgList[0].lower().strip()

                elif msg.startswith("ERROR"):
                    command = msgList[0]
                    message = msgList[2]

                else:
                    raise InvalidIRCResponse("no starting colon")

            else:

                msgSplit = msgList[0].split()

                message = msgList[2]

                try:
                    source  = msgSplit[0]
                except IndexError:
                    raise InvalidIRCResponse("no source")

                try:
                    command = msgSplit[1].lower().strip()
                except IndexError:
                    raise InvalidIRCResponse("no command")

                args = msgSplit[2:]


            if "@" in source:
                sourceFull = source
                sourceP    = source.partition("@")
                sourceHost = sourceP[2]
                sourceU    = sourceP[0].partition("!")
                source     = sourceU[0]
                sourceUser = sourceU[2]

        self.source     = source
        self.sourceFull = sourceFull
        self.sourceHost = sourceHost
        self.sourceUser = sourceUser
        self.command    = command
        self.args       = args
        self.message    = message

    @property
    def isResponse(self):
        return True



    @property
    def isMessage(self):
        return False

    @property
    def canBeMessage(self):
        return (self.command == "privmsg" and bool(self.message))



    @property
    def isCTCPMessage(self):
        return False

    @property
    def canBeCTCPMessage(self):
        return (self.canBeMessage and (self.message.startswith("\x01") and
                self.message.endswith("\x01") ) )



    @property
    def isNotice(self):
        return False

    @property
    def canBeNotice(self):
        return (self.command == "notice" and bool(self.message))



    @property
    def isCTCPNotice(self):
        return False

    @property
    def canBeCTCPNotice(self):
        return (self.canBeNotice and (self.message.startswith("\x01") and
                self.message.endswith("\x01") ) )



    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, repr(self.response) )

    def __str__(self):
        ret = [self.source, self.command, self.args, self.message]
        return str(ret)

