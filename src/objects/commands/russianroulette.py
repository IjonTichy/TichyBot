#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
class RussianRoulette(object):

    def __init__(self, chambers=6):
        self.chambers = chambers
        self.chamber  = 1
        self.loaded   = False

        self.loadBullet()
        self.spinChambers(10, 20)


    def loadBullet(self):
        self.bullet = (self.chambers // 2) + 1
        self.loaded = True

    def spinChambers(self, low, hi):
        spins   = random.randint(low, hi)
        newBul  = (self.bullet + spins) % self.chambers

        if newBul == 0:
            newBul = self.chambers

        self.bullet = newBul
        self.chamber = 1


    def fire(self):
        bang = False

        if (self.chamber == self.bullet) and self.loaded:
            bang = True
            self.loaded = False

        self.chamber += 1

        return bang


    @property
    def bullet(self):
        return self.__bullet

    @bullet.setter
    def bullet(self, chamber):
        assert 1 <= chamber <= self.chambers, "can't put bullet in nonexistent chamber {}".format(chamber)
        self.__bullet = chamber


    @property
    def loaded(self):
        return self.__loaded

    @loaded.setter
    def loaded(self, cond):
        assert cond in (True, False), "must be loaded or not loaded, not {}".format(cond)
        self.__loaded = cond
