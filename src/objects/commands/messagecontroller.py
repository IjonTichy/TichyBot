#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects import irccommand
from objects.commands import messagecommand
from functions import getusers, highestresponse

import os

USERDIR = os.getenv("HOME") + "/tichybot/USERS"

class MessageController(messagecommand.MessageCommand):

    TRIGGER = ("join", "part", "leave", "say", "quit")

    def __init__(self):
        super().__init__()

        self.commands = {"join": self.join, "part": self.part,
                         "leave": self.part, "say": self.say,
                         "quit": self.quit}

        self.channels = set()



    def processLine(self, line):
        super().processLine(line)

        ret = highestresponse.highestResponse(line)

        if ret.command == "join" and ret.source == self.master.name:
            self.channels |= {ret.message}



    def respond(self, response):
        msg     = response.message
        trigger = msg.split(" ")[0]

        source = response.source
        target = response.target

        if target.startswith("#"):   # directed to channel, pay no heed
            return

        if source not in getusers.getUsers(USERDIR):    # fuck off
            return

        if trigger in self.commands:
            return self.commands[trigger](response)
        else:
            return "Ghost command {}".format(trigger)


    def join(self, response):
        msg     = response.message
        channel = msg.split(" ")[1]

        joinCommand = irccommand.IRCCommand("JOIN", [channel])
        self.master.sendCommand(joinCommand)

        self.channels |= {channel}


    def part(self, response):
        msg      = response.message
        msgSplit = msg.split(" ")
        channel   = msgSplit[1]
        message   = " ".join(msgSplit[2:])

        if channel in self.channels:
            print("will part")
            partCommand = irccommand.IRCCommand("PART", [channel], message)
            self.master.sendCommand(partCommand)

            self.channels -= {channel}

        else:
            return "Not in {}".format(channel)


    def say(self, response):
        msg       = response.message
        msgSplit  = msg.split(" ")
        channel   = msgSplit[1]
        message   = " ".join(msgSplit[2:])


        if channel in self.channels or not channel.startswith("#"):   # it might not actually be a channel!
            sayCommand = irccommand.IRCCommand("PRIVMSG", [channel], message)
            self.master.sendCommand(sayCommand)

        else:
            return "Not in {}".format(channel)


    def quit(self, response):
        msg       = response.message
        reason    = msg.split(" ")[1:]
        reason    = " ".join(reason)

        if not reason:
            self.master.quit("From {} - quitting".format(response.source) )

        else:
            self.master.quit(reason)
