#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from . import basebot

from .listeners import (messagelistener, noticelistener, joinlistener,
                        partlistener, pinglistener, quitlistener, kicklistener,
                        versionlistener, nicklistener, cannotsendlistener,
                        motdlistener, modelistener)


class ChatBot(basebot.BaseBot):

    def __init__(self, server, port, master):

        super().__init__(server, port, master)

        self.name      = "TestChatBot"
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
                        modelistener.ModeListener(),
                        ]
