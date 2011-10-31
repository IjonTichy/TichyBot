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
        self.game  = russianroulette.RussianRoulette()

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
        self.game.spinChambers(10, 20)
        return "{} spins the chambers.".format(response.source)

    def fire(self, response):
        dead = self.game.fire()

        if dead:
            kickCommand = irccommand.IRCCommand("KICK", [response.target, response.source], "*BANG*")
            self.master.sendCommand(kickCommand)

            return "{} loses.".format(response.source)

        else:
            return "The revolver clicks."

    def load(self, response):

        if self.game.loaded:
            self.game.loaded = False

            kickCommand = irccommand.IRCCommand("KICK", [response.target, response.source], "*BANG*")
            self.master.sendCommand(kickCommand)
            return "{} looked into the barrel.".format(response.source)

        else:
            self.game.loadBullet()
            self.game.spinChambers(10, 20)
            return "{} loads the gun and spins the chambers.".format(response.source)

    def loaded(self, response):
        if self.game.loaded:
            return "The gun is loaded."
        else:
            return "The gun is empty."

    def help(self, response):
        return helpStr
