
import sys, copy
import hangmanletter

class InvalidWord(Exception): pass

class HangmanWord(object):

    def __init__(self, word, maxGuesses=10):

        self.__word       = word.lower()
        self.__letters    = []
        self.__guessed    = []
        self.__maxGuesses = maxGuesses
        self.__spaceCount = 0
        self.__guessCount = 0
        self.__isPhrase   = False

        for letter in self.__word:
            try:
                hLetter = hangmanletter.HangmanLetter(letter)

            except hangmanletter.InvalidLetter:
                raise InvalidWord(sys.exc_info()[1])

            else:
                if hLetter.isWhitespace:
                    hLetter.reveal()
                    self.__spaceCount += 1

                self.__letters.append(hLetter)

        for letter in self.letters:
            if not letter.isWhitespace:
                break
        else:
            raise InvalidWord("must contain at least one non-whitespace character")


    def guessLetter(self, guess):

        ret = {"alreadyGuessed": False, "valid": False, "correct": False, "count": 0}

        guess = guess.lower()

        if not guess:
            return ret

        if guess in self.__guessed:
            ret["alreadyGuessed"] = True
            return ret
        else:
            self.__guessed.append(guess)

        try:
            HangmanWord(guess)
        except InvalidWord:
            return ret

        ret["valid"] = True

        for letter in self.__letters:

            if letter == guess:
                ret["correct"] = True

                if not letter.revealed:
                    ret["count"] += 1
                    letter.reveal()

        if not ret["correct"]:
            self.__guessCount += 1

        return ret

    def guessWord(self, guess):

        ret = {"alreadyGuessed": False, "valid": False, "correct": False, "isWord": False, "count": 0}

        guess = guess.lower()

        if not guess:
            return ret

        if guess in self.__guessed:
            ret["alreadyGuessed"] = True
            return ret
        else:
            self.__guessed.append(guess)

        try:
            HangmanWord(guess)
        except InvalidWord:
            return ret

        ret["valid"] = True

        if self.__word == guess:
            ret["isWord"]  = True

        last = 0
        next = 0

        while True:
            next = self.__word.find(guess, last)

            if next == -1:
                break

            last = next + 1

            ret["correct"] = True

            for let in self.__letters[next:next+len(guess)]:

                if not let.revealed:
                    let.reveal()
                    ret["count"] += 1

        if not ret["correct"]:
            self.__guessCount += 1

        return ret

    @property
    def allRevealed(self):

        for letter in self.__letters:
            if not letter.revealed:
                return False
        else:
            return True

    @property
    def guessed(self):
        return copy.deepcopy(self.__guessed)

    @property
    def word(self):
        return self.__word

    @property
    def letters(self):
        return copy.deepcopy(self.__letters)

    @property
    def maxGuesses(self):
        return self.__maxGuesses


    @maxGuesses.setter
    def maxGuesses(self, newMax):

        newMax = int(newMax)

        if newMax > 0:
            self.__maxGuesses = newMax
        else:
            raise ValueError("max guess count <= 0")

    @property
    def isPhrase(self):
        return self.__isPhrase

    @property
    def term(self):
        return "phrase" if self.__isPhrase else "word"

    @property
    def guessCount(self):
        return self.__guessCount

    @guessCount.setter
    def guessCount(self, newCount):

        newCount = int(newCount)

        if (newCount > 0) and (newCount <= self.__maxGuesses):
            self.__guessCount = newCount
        else:
            if newCount <= 0:
                raise ValueError("guess count <= 0")
            else:
                raise ValueError("guess count > max guess count")


    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__, repr(self.__word),
                                      repr(self.__maxGuesses))

    def __str__(self):

        ret  = "({0}/{1}) {2} ({3})"
        word = ""
        gues = ""
        guessL = []

        for letter in self.__letters:
            word += str(letter)


        for guess in self.__guessed:
            guessL.append(repr(guess) )

        gues = ", ".join(guessL)

        return ret.format(self.__guessCount, self.__maxGuesses, word, gues)

    def __len__(self):
        return len(self.__word) - self.__spaceCount

