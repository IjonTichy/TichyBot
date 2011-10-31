#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse
from functions import ansicodes

SB = ansicodes.BOLDON
EB = ansicodes.BOLDOFF

class TopicListener(baselistener.BaseListener):

    def processLine(self, line):
        msg333   = "Topic for {} set by {} on {}"

        msg332   = "Topic for " + SB + "{}" + EB + " is ", "\"{}\""
        msg332C  = "-",                                    "6"

        msgTopic = "Topic for " + SB + "{}" + EB + " changed to ", "\"{}\"", " by ", "{}"
        msgTopicC= "-",                                            "6",      "-",    "G"

        ret = ircresponse.IRCResponse(line)

        if ret.command == "332":
            topic  = ret.message
            channel = ret.args[1]

            msg = ansicodes.mapColors(msg332, msg332C)

            self.master.log(msg.format(channel, topic))

        if ret.command == "topic":
            setter  = ret.source
            channel = ret.args[0]
            topic   = ret.message

            msg = ansicodes.mapColors(msgTopic, msgTopicC)

            self.master.log(msg.format(channel, topic, setter))


