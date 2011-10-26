#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from .. import basebot
from ..listeners import (messagelistener, joinlistener, partlistener, pinglistener,
                        quitlistener, kicklistener, versionlistener, nicklistener,
                        cannotsendlistener, noticelistener)

from ..tochan import    tochanlistener
from ..storechan import storechanlistener

from . import hangmanlistener


class HangmanBot(basebot.BaseBot):

    def __init__(self, server, port, master):

        super().__init__(server, port, master)

        self.name      = "TestHangBot"
        self.uName     = "tichybot"
        self.rName     = "Hang Tichy Bot"
        self.listeners =[
                        messagelistener.MessageListener(),
                        noticelistener.NoticeListener(),
                        joinlistener.JoinListener(),
                        partlistener.PartListener(),
                        pinglistener.PingListener(),
                        quitlistener.QuitListener(),
                        kicklistener.KickListener(),
                        versionlistener.VersionListener(),
                        nicklistener.NickListener(),
                        cannotsendlistener.CannotSendListener(),
                        tochanlistener.ToChanListener(),
                        storechanlistener.StoreChanListener()
                        ]
