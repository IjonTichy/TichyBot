import os
import shelve

class InvalidScore(Exception): pass

class ScoreKeeper(object):

    def __init__(self, scorePath="./scores.dbm"):

        self.__scorePath = os.path.abspath(scorePath)
        self.__scores = shelve.open(self.__scorePath, flag="c")


    def __checkScoreExists(self, name, default=0):
        name = name.lower()

        if name not in self:
            self[name] = default


    def setPoints(self, name, amount):
        name = name.lower()

        amount = int(amount)

        self[name] = amount

    def givePoints(self, name, amount):
        name = name.lower()

        self.__checkScoreExists(name)

        amount = int(amount)


        self[name] += amount

    def takePoints(self, name, amount):
        name = name.lower()

        self.__checkScoreExists(name)

        amount = int(amount)

        self[name] -= amount


    def resetScores(self):
        for score in self:
            del self[score]

    def sync(self):
        self.__scores.sync()





    def __del__(self):
        self.__scores.sync()
        self.__scores.close()

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, repr(self.__scoreDir))

    def __str__(self):
        ret = "Scores:\n"
        scores = []

        for score in sorted(self, key=(lambda x: self[x]), reverse=True):
            scores.append("{0:^15} - {1}".format(score, self[score]) )

        if not scores:
            scores = ["<none>"]

        ret += "\n".join(scores)

        return ret


    def __getitem__(self, item):
        return self.__scores[item]

    def __setitem__(self, item, setTo):
        self.__scores[item] = setTo

    def __delitem__(self, item):
        del self.__scores[item]

    def __contains__(self, item):
        return True if (item in self.__scores) else False

    def __iter__(self):
        return iter(self.__scores)
