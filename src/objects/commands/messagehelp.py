#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand

helpStr = """
Commands (% = Russian Roulette, needs kick privileges to work properly):
  !tp (bc|dice|fortune|help|info|uptime|version)
  %fire %help %load %loaded %spin
"""

class MessageHelp(messagecommand.MessageCommand):

    TRIGGER = "!tb help"

    def respond(self, response):
        return helpStr
