#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VOWELS     = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def pluralise(word, cond, assumePlural=True):

    word = word.lower()

    if cond == 1:
        return word

    ##
    #  Special cases

    if word == "ox":
        return "oxen"

    if word == "sheep":
        return word

    ##
    #  General cases

    if word[-1:] == "s":
        if assumePlural:
            return word
        else:
            return word + "'"

    if word[-1:] == "x":
        return word + "es"

    if word[-1:] == "o" and word[-2:-1] in CONSONANTS:
        return word + "es"

    if word[-1:] == "y" and word[-2:-1] in CONSONANTS:
        return word[:-1] + "ies"

    if word[-2:] == "fe":
        return word[:-2] + "ves"

    if word[-2:] == "sh":
        return word + "es"

    # Last ditch effort
    return word + "s"
