#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
from functions import getversion

import os

VERSIONDIR = os.getenv("HOME") + "/tichybot/VERSION"

class MessageVersion(messagecommand.MessageCommand):

    TRIGGER = "!tb version"

    def respond(self, response):
        return getversion.getVersion(VERSIONDIR)
