#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from objects import basebot
from objects.listeners import (messagelistener, noticelistener, joinlistener,
                        partlistener, pinglistener, quitlistener, kicklistener,
                        versionlistener, nicklistener, cannotsendlistener,
                        motdlistener, modelistener, topiclistener)

from objects.commands import (messageversion, messageuptime, messagedice,
                              messagefortune, messagebc, messageinfo,
                              messageroulette, messagehelp, messagecontroller)

class CommandBot(basebot.BaseBot):

    def __init__(self, server, port, master):

        super().__init__(server, port, master)

        self.name      = "tichybot"
        self.uName     = "tichybot"
        self.rName     = "Tichybot"
        self.listeners =[
                        # ~ messagelistener.MessageListener(),
                        # ~ noticelistener.NoticeListener(),
                        # ~ joinlistener.JoinListener(),
                        # ~ partlistener.PartListener(),
                        # ~ quitlistener.QuitListener(),
                        # ~ kicklistener.KickListener(),
                        # ~ nicklistener.NickListener(),
                        # ~ motdlistener.MOTDListener(),
                        # ~ cannotsendlistener.CannotSendListener(),
                        # ~ modelistener.ModeListener(),
                        # ~ topiclistener.TopicListener(),
                        messageversion.MessageVersion(),
                        messagehelp.MessageHelp(),
                        messageinfo.MessageInfo(),
                        messageuptime.MessageUptime(),
                        messagebc.MessageBC(),
                        messagedice.MessageDice(),
                        messagefortune.MessageFortune(),
                        messageroulette.MessageRoulette(),
                        messagecontroller.MessageController(),
                        ]
