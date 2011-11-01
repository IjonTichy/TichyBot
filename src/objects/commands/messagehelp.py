#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
from functions import getversion

import os

HELPDIR = os.getenv("HOME") + "/tichybot/HELP"

class MessageHelp(messagecommand.MessageCommand):

    TRIGGER = "!tb help"

    def respond(self, response):
        return getversion.getVersion(HELPDIR)
