#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import basebot
from .listeners import (messagelistener, joinlistener, partlistener, pinglistener,
                       quitlistener, kicklistener, versionlistener)


class ChatBot(basebot.BaseBot):

    def __init__(self, server, port, master):

        super().__init__(server, port, master)

        self.name      = "TestChatBot"
        self.uName     = "tichybot"
        self.rName     = "Chat Tichy Bot"
        self.listeners = [messagelistener.MessageListener(), joinlistener.JoinListener(),
                          partlistener.PartListener(), pinglistener.PingListener(),
                          quitlistener.QuitListener(), kicklistener.KickListener(),
                          versionlistener.VersionListener()]

        self.currentData = ""
