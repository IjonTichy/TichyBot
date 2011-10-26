
import string

usableChars = string.ascii_letters + string.digits + string.whitespace

class InvalidLetter(Exception): pass

class HangmanLetter(object):

    NOTREVEALED = "-"

    def __init__(self, letter, revealed=False):

        if letter not in usableChars:
            raise InvalidLetter("\"{0}\" is not a valid letter".format(letter) )

        self.__letter   = letter
        self.__revealed = bool(revealed)
        self.__isWhitespace = (self.__letter in string.whitespace)

    @property
    def revealed(self):
        return self.__revealed

    @property
    def letter(self):
        return self.__letter

    @property
    def isWhitespace(self):
        return self.__isWhitespace


    def reveal(self):
        self.__revealed = 1

    # there is no need for this I think
    def unreveal(self):
        self.__revealed = 0

    def guess(self, letter):
        if letter == self.letter:
            self.reveal()
            return True
        else:
            return False


    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, repr(self.__letter), self.__revealed)

    def __str__(self):
        return self.letter if self.revealed else HangmanLetter.NOTREVEALED

    def __eq__(self, other):
        return self.letter == other

    def __ne__(self, other):
        return self.letter != other
