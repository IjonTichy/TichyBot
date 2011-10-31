#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
from functions import getinfo

import os

INFODIR = os.getenv("HOME") + "/tichybot/INFO"

class MessageInfo(messagecommand.MessageCommand):

    TRIGGER = "!tb info"

    def respond(self, response):
        return getinfo.getInfo(INFODIR)
