#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import threading
import socket
import time
import os
from . import botthread
from . import irccommand
from .listeners import echolistener, argecholistener
from functions import ansicodes

BASELOGDIR = os.path.abspath("../logs")

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
                listener.process(newLines, self)

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


    def sendCommand(self, commandObj):

        for listener in self.listeners:
            listener.processAction(commandObj, self)

        data = str(commandObj) + "\n"
        sData = bytes(data, encoding="utf-8")

        self.socket.send(sData)

    #######
    ###
    ##  MESSAGING
    ###
    #######


    def sendMessage(self, data):

        if not data:
            return

        dataSplit = data.partition(":")
        dataList  = [i for i in dataSplit[0].split() if i]

        try:
            command = dataList[0]
            args    = dataList[1:]
            message = dataSplit[2]
        except:
            self.log("Invalid command '{}'".format(data) )
        else:
            ircCommand = irccommand.IRCCommand(command, args, message)
            self.sendCommand(ircCommand)


    #######
    ###
    ##  LOGGING
    ###
    #######

    def writeToLog(self, line):
        cTime      = time.gmtime()
        cDate = time.strftime("%Y-%m-%d", cTime)

        logdir = BASELOGDIR
        olddir = os.getcwd()

        try:
            os.makedirs(logdir)
        except OSError:
            pass

        os.chdir(logdir)

        line = ansicodes.stripCodes(line)

        log = open(cDate + ".txt", "a")
        log.write(line + "\n")
        log.close()

        os.chdir(olddir)



    def log(self, line):
        cTime      = time.gmtime()
        cTimestamp = time.strftime("<%H:%M>", cTime)

        newline = "{} {}".format(cTimestamp, line)

        self.writeToLog(newline)
        print(newline)


    #######
    ###
    ##  EXITING
    ###
    #######


    def quit(self, reason):
        self.sendData("QUIT :\"{}\"".format(reason) )
        self.remove()

    def remove(self):
        cTime      = time.gmtime()
        cTimestamp = time.strftime("<%H:%M>", cTime)

        self.log("!!! Exiting")
        del self

