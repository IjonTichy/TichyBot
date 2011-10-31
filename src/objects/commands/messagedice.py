#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects.commands import messagecommand
from functions import dice

import os

INFODIR = os.getenv("HOME") + "/tichybot/INFO"

class MessageDice(messagecommand.MessageCommand):

    TRIGGER = "!tb dice"

    def respond(self, response):
        command = response.message.lstrip(self.__class__.TRIGGER).strip()

        if not command:
            return

        command = command.split(" ")

        return dice.main(command)
