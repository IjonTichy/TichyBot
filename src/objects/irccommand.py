#!/usr/bin/env python3

# -*- coding: utf-8 -*-

class IRCCommand(object):

    def __init__(self, command, args=[], message=""):

        self.command = command
        self.args    = args
        self.message = message


    @property
    def command(self):
        return self.__command

    @property
    def args(self):
        return self.__args

    @property
    def message(self):
        return self.__message


    @command.setter
    def command(self, new):
        assert isinstance(new, str), "command must be str, not {}".format(new.__class__.__name__)
        self.__command = new.lower()

    @args.setter
    def args(self, new):
        assert isinstance(new, list),  "args must be list, not {}".format(new.__class__.__name__)
        self.__args = new

    @message.setter
    def message(self, new):
        assert isinstance(new, str), "message must be str, not {}".format(new.__class__.__name__)
        self.__message = new


    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join(repr(x) for x
                               in (self.command, self.args, self.message) ) )

    def __str__(self):

        cmd = self.command.upper()

        if self.args and self.message:
            return "{} {} :{}".format(cmd, " ".join(self.args), self.message)

        elif self.args:
            return "{} {}".format(cmd, " ".join(self.args))

        elif self.message:
            return "{} {}".format(cmd, self.message)

        else:
            return "{}".format(cmd)
