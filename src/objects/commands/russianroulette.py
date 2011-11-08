#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Full(Exception): pass
class InvalidChamber(Exception): pass

class RussianRoulette(object):

    def __init__(self, chambers=6):
        self.chambers = chambers
        self.chamber  = 0
        self.bullets  = [False] * self.chambers

        self.loadBullet()
        self.spinChambers(10, 20)


    def loadBullet(self):
        newBullet = 0

        while self.bulletIn(newBullet):
            newBullet += 1

            if newBullet == self.chambers:
                raise Full("no chambers left")

        self.addBullet(newBullet)


    def spinChambers(self, low, hi):
        spins   = random.randint(low, hi) % self.chambers

        self.__spin(spins)


    def fire(self):
        bang = False

        if (self.bulletIn(0)) and self.loaded:
            bang = True
            self.removeBullet(self.chamber)

        self.__spin(1)

        return bang

    def bulletIn(self, chamber):
        return True in self.bullets[chamber:chamber+1]


    def addBullet(self, chamber):
        if 0 > chamber or self.chambers <= chamber:
            raise InvalidChamber()

        self.bullets[chamber] = True


    def removeBullet(self, chamber):
        if 0 > chamber or self.chambers <= chamber:
            raise InvalidChamber()

        self.bullets[chamber] = False


    def __spin(self, amount):

        spinCount = amount % self.chambers

        bul = self.bullets
        bul = bul[-spinCount:] + bul[:-spinCount]
        self.bullets = bul


    @property
    def loaded(self):
        return True in self.bullets

    @property
    def bulletCount(self):
        return sum(self.bullets)
