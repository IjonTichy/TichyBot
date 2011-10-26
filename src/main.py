#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects import botcontroller
from objects import basebot, chatbot
from objects.hangbot import hangmanbot

SERVER = "crimson.lostsig.net"
# ~ SERVER = "irc.skulltag.com"
PORT   = 6667

if __name__ == "__main__":
    controller = botcontroller.BotController()

    bot = hangmanbot.HangmanBot(SERVER, PORT, controller)
    # ~ bot = chatbot.ChatBot(SERVER, PORT, controller)
    # ~ bot = basebot.BaseBot(SERVER, PORT)

    botNum = controller.startBot(bot)

    while True:
        try:
            msg = input("")

            if controller.botAlive(botNum):
                controller.sendTo(botNum, msg)
            else:
                break

        except KeyboardInterrupt:
            print()

        except EOFError:
            print("^D")
            controller.sendTo(botNum, "quit")
            break
