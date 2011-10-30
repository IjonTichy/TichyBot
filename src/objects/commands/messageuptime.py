#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
import os

class MessageUptime(messagecommand.MessageCommand):

    TRIGGER = "!tb uptime"

    def respond(self, response):
        uptime = os.popen("uptime")
        ret = uptime.read()

        return ret.strip()
