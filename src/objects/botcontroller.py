#!/usr/bin/env python3

# -*- coding: utf-8 -*-


import copy

class BotController(object):

    THREADBASE = "TichyThread-{}"

    def __init__(self):
        self.__childBots = {}


    def __del__(self):
        for i in self.__childBots:
            self.stopBot(i)

        del self.__childBots

    #######
    ###
    ##  PROPERTIES
    ###
    #######

    @property
    def server(self):
        return self.__server

    @property
    def port(self):
        return self.__port

    @server.setter
    def server(self, new):

        assert isinstance(new, str), "server must be str, not {}".format(new.__class__.__name)
        self.__server = new

    @port.setter
    def port(self, new):

        assert isinstance(new, int), "port must be int, not {}".format(new.__class__.__name)
        self.__port = new

    @property
    def childBots(self):
        return copy.deepcopy(self.__childBots)

    #######
    ###
    ##  BOT CONTROL
    ###
    #######

    def startBot(self, bot):
        botNum = 0

        while botNum in self.__childBots:
            botNum += 1

        self.__childBots[botNum] = bot
        self.__childBots[botNum].start()

        return botNum


    def stopBot(self, botNum):
        assert botNum in self.__childBots, "no such bot index"
        self.__childBots[botNum].stop()


    def restartBot(self, botNum):
        assert botNum in self.__childBots, "no such bot index"
        self.__childBots[botNum].start()


    def botAlive(self, botNum):
        assert botNum in self.__childBots, "no such bot index"
        return self.__childBots[botNum].isAlive()


    def sendTo(self, botNum, message):
        assert botNum in self.__childBots, "no such bot index"
        self.__childBots[botNum].sendMessage(message)
