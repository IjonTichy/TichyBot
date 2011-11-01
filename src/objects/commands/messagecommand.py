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

        trigger = self.__class__.TRIGGER
        toMe = False

        if isinstance(trigger, str):
            if msg.startswith(self.__class__.TRIGGER):
                toMe = True

        elif isinstance(trigger, (list, tuple)):

            for i in trigger:
                if msg.startswith(i):
                    toMe = True
                    break        # we're done here

        if toMe:
            response = self.respond(ret)

            if not response:
                return

            cmd = irccommand.IRCCommand("PRIVMSG", [], "")

            if toChan:
                cmd.args = [rec]
            else:
                cmd.args = [src]

            for line in response.split("\n"):
                line = line.rstrip()

                if line:
                    cmd.message = line
                    print(cmd)
                    self.master.sendCommand(cmd)
