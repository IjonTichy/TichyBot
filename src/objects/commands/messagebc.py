#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from objects import fakefile
from objects.commands import messagecommand
from subprocess import PIPE, Popen

class MessageBC(messagecommand.MessageCommand):

    TRIGGER = "!tb bc"

    def respond(self, response):

        command = response.message.lstrip(self.__class__.TRIGGER).strip()
        command += "\n"

        if not command:
            return "MessageBC: must provide bc command"

        bc = Popen(("bc", "-l"), stdin=PIPE, stdout=PIPE, stderr=PIPE)

        sInput, sOutput, sErr = bc.stdin, bc.stdout, bc.stderr

        sInput.write(command.encode("utf-8"))
        sInput.close()

        out = sOutput.read().decode()
        err = sErr.read().decode()

        if err:
            err = err.replace("\n", " ")
            return err
        else:
            out = out.replace("\n", " ")
            return out
