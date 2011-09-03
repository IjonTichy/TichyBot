#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import threading
import socket
import time
import os
from . import botthread
from . import irccommand
from .listeners import echolistener, argecholistener

BASELOGDIR = "/home/edrik/tichybot/logs"

class BaseBot(botthread.BotThread):

    def __init__(self, server, port, master):

        super().__init__()

        self.server    = server
        self.port      = port
        self.socket    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name      = "TestTichyBot"
        self.uName     = "tichybot"
        self.rName     = "Test Tichy Bot"
        self.listeners = [echolistener.EchoListener(), argecholistener.ArgEchoListener()]

        self.currentData = ""

        self.master = master

    #######
    ###
    ##  MAIN
    ###
    #######


    def run(self):
        self.connect()

        while not self.stopped:
            data = self.receiveData()

            self.addToData(data)
            newLines = self.getNewLines()

            for listener in self.listeners:
                response = listener.process(newLines, self)

            if ":Closing link:" in data:   # Connection ded :(
                self.remove()
                return

        self.quit("Quitting")

    #######
    ###
    ##  CONNECTING
    ###
    #######


    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect( (self.server, self.port) )
        self.socket.setblocking(False)

        nickSend = irccommand.IRCCommand("NICK", [], "")
        userSend = irccommand.IRCCommand("USER", [self.uName, self.uName, "*"], self.rName)

        self.receiveData()

        response = ":Nickname is already in use."

        tName = self.name

        while True:
            nickSend.args = [tName]
            self.sendCommand(nickSend)

            response = self.receiveData()

            if ":Nickname is already in use." in response:
                tName += "_"
            else:
                break

        self.name = tName

        self.sendCommand(userSend)

    #######
    ###
    ##  DATA
    ###
    #######

    def addToData(self, newData):
        self.currentData += newData

    def getNewLines(self):
        ret = self.currentData.rpartition("\n")

        self.currentData = ret[2]

        return ret[0]


    #######
    ###
    ##  SOCKET
    ###
    #######


    def receiveData(self, buf=4096, timeout=1):

        try:
            ret = self.socket.recv(buf)

        except socket.error:
            ret = b""

        ret = ret.decode()
        ret = ret.replace("\r\n", "\n")
        ret2 = ""

        for char in ret:
            if ord(char) <= 127:
                ret2 += char
            else:
                ret2 += "?"

        return ret2

    def sendRaw(self, data):

        data += "\n"

        sData = bytes(data, encoding="utf-8")

        self.socket.send(sData)


    def sendCommand(self, commandObj):
        self.sendRaw(str(commandObj))


    #######
    ###
    ##  MESSAGING
    ###
    #######


    def sendMessage(self, data):
        self.sendRaw(data)


    #######
    ###
    ##  LOGGING
    ###
    #######

    def writeToLog(self, line):
        date = time.strftime("%Y-%m-%d")

        logdir = BASELOGDIR
        olddir = os.getcwd()

        try:
            os.makedirs(logdir)
        except OSError:
            pass

        os.chdir(logdir)

        log = open(date + ".txt", "a")
        log.write(line + "\n")
        log.close()

        os.chdir(olddir)



    def log(self, line):

        self.writeToLog(line)
        print(line)


    #######
    ###
    ##  EXITING
    ###
    #######


    def quit(self, reason):
        self.sendData("QUIT :{}".format(reason) )
        self.remove()

    def remove(self):
        cTime      = time.gmtime()
        cTimestamp = time.strftime("<%H:%M>", cTime)

        self.log("{} !!! Exiting".format(cTimestamp) )
        del self

