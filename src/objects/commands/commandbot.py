#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from objects import basebot
from objects.listeners import (messagelistener, noticelistener, joinlistener,
                        partlistener, pinglistener, quitlistener, kicklistener,
                        versionlistener, nicklistener, cannotsendlistener,
                        motdlistener)

from objects.commands import (messageversion, messageuptime)


class CommandBot(basebot.BaseBot):

    def __init__(self, server, port, master):

        super().__init__(server, port, master)

        self.name      = "tichybot"
        self.uName     = "tichybot"
        self.rName     = "Chat Tichy Bot"
        self.listeners =[
                        messagelistener.MessageListener(),
                        noticelistener.NoticeListener(),
                        joinlistener.JoinListener(),
                        partlistener.PartListener(),
                        quitlistener.QuitListener(),
                        kicklistener.KickListener(),
                        versionlistener.VersionListener(),
                        nicklistener.NickListener(),
                        motdlistener.MOTDListener(),
                        cannotsendlistener.CannotSendListener(),
                        messageversion.MessageVersion(),
                        messageuptime.MessageUptime(),
                        ]
