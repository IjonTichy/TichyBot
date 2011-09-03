#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from . import baselistener
from .. import ircresponse

class ArgEchoListener(baselistener.BaseListener):

    def processLine(self, line):
        ret = ircresponse.IRCResponse(line)

        print(ret.source, ret.command, ret.args, ret.message)

