#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects import irccommand
from objects.commands import messagecommand, russianroulette
from subprocess import PIPE, Popen

helpStr = """
Russian Roulette - needs kick privileges to function properly
Commands: %fire %help %load %loaded %spin
"""


class MessageRoulette(messagecommand.MessageCommand):

    TRIGGER = ("%spin", "%fire", "%load", "%loaded", "%help")

    def __init__(self):
        super().__init__()
        self.games = {}

        self.funcs = {"%spin": self.spin, "%fire": self.fire,
                      "%load": self.load, "%loaded": self.loaded,
                      "%help": self.help}

    def respond(self, response):

        msg     = response.message
        trigger = msg.split(" ")[0]

        if trigger in self.funcs:
            return self.funcs[trigger](response)
        else:
            return "Ghost command {}".format(trigger)

    def spin(self, response):

        chan = response.target

        if not chan.startswith("#"):
            return "I don't feel like giving you a gun."

        elif chan not in self.games:
            return "You need a gun to spin the chambers of (use %load)."

        game = self.games[chan]

        game.spinChambers(10, 20)
        return "{} spins the chambers.".format(response.source)

    def fire(self, response):

        chan = response.target

        if not chan.startswith("#"):
            return "Private games don't work too well."

        elif chan not in self.games:
            return "But you haven't got a gun! (%load will get one for you)"

        game = self.games[chan]

        dead = game.fire()

        if dead:
            kickCommand = irccommand.IRCCommand("KICK", [response.target, response.source], "*BANG*")
            self.master.sendCommand(kickCommand)

            return "{} loses.".format(response.source)

        else:
            return "The revolver clicks."

    def load(self, response):

        chan = response.target

        if not chan.startswith("#"):
            return "I don't feel like giving you a gun."

        elif chan not in self.games:
            self.games[chan] = russianroulette.RussianRoulette()
            return "{} fetches a loaded gun.".format(response.source)

        game = self.games[chan]

        if game.loaded:
            game.loaded = False

            kickCommand = irccommand.IRCCommand("KICK", [response.target, response.source], "*BANG*")
            self.master.sendCommand(kickCommand)
            return "{} looked into the barrel.".format(response.source)

        else:
            game.loadBullet()
            game.spinChambers(10, 20)
            return "{} loads the gun and spins the chambers.".format(response.source)

    def loaded(self, response):

        chan = response.target

        if not chan.startswith("#"):
            return "We aren't playing a game - go away."

        elif chan not in self.games:
            return "There is no gun to check (%load gets one)."

        game = self.games[chan]

        if game.loaded:
            return "The gun is loaded."
        else:
            return "The gun is empty."

    def help(self, response):
        return helpStr
