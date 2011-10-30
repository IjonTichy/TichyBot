#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.listeners import baselistener
from objects import irccommand
from functions import highestresponse

class MessageCommand(baselistener.BaseListener):

    def processLine(self, line):

        ret = highestresponse.highestResponse(line)

        if not ret.isMessage:
            return

        msg = ret.message
        src = ret.source
        rec = ret.target

        if rec.startswith("#"):
            toChan = True
        else:
            toChan = False

        if msg.startswith(self.__class__.TRIGGER):

            response = self.respond(ret)

            cmd = irccommand.IRCCommand("PRIVMSG", [], response)

            if toChan:
                cmd.args = [rec]
            else:
                cmd.args = [src]

            self.master.sendCommand(cmd)
