#!/usr/bin/python3

# -*- coding: utf-8 -*-

ANSISTART = "\033["
ANSIEND   = "m"

RESET               = ANSISTART + "0"  + ANSIEND

BOLDON              = ANSISTART + "1"  + ANSIEND
BOLDOFF             = ANSISTART + "22" + ANSIEND

DIMON               = ANSISTART + "2"  + ANSIEND
DIMOFF              = ANSISTART + "21" + ANSIEND

ITALICSON           = ANSISTART + "3"  + ANSIEND
ITALICSOFF          = ANSISTART + "23" + ANSIEND

UNDERLINEON         = ANSISTART + "4"  + ANSIEND
UNDERLINEOFF        = ANSISTART + "24" + ANSIEND

BLINKON             = ANSISTART + "5"  + ANSIEND
BLINKONFAST         = ANSISTART + "6"  + ANSIEND   # not widely supported
BLINKOFF            = ANSISTART + "25" + ANSIEND

INVERSEON           = ANSISTART + "7"  + ANSIEND
INVERSEOFF          = ANSISTART + "27" + ANSIEND

STRIKETHROUGHON     = ANSISTART + "7"  + ANSIEND
STRIKETHROUGHOFF    = ANSISTART + "27" + ANSIEND

BLACKF              = ANSISTART + "30" + ANSIEND
REDF                = ANSISTART + "31" + ANSIEND
GREENF              = ANSISTART + "32" + ANSIEND
YELLOWF             = ANSISTART + "33" + ANSIEND
BLUEF               = ANSISTART + "34" + ANSIEND
MAGENTAF            = ANSISTART + "35" + ANSIEND
CYANF               = ANSISTART + "36" + ANSIEND
WHITEF              = ANSISTART + "37" + ANSIEND
DEFAULTF            = ANSISTART + "39" + ANSIEND

BLACKB              = ANSISTART + "40" + ANSIEND
REDB                = ANSISTART + "41" + ANSIEND
GREENB              = ANSISTART + "42" + ANSIEND
YELLOWB             = ANSISTART + "43" + ANSIEND
BLUEB               = ANSISTART + "44" + ANSIEND
MAGENTAB            = ANSISTART + "45" + ANSIEND
CYANB               = ANSISTART + "46" + ANSIEND
WHITEB              = ANSISTART + "47" + ANSIEND
DEFAULTB            = ANSISTART + "49" + ANSIEND

fgColors = {"0": BOLDOFF + DIMOFF + BLACKF, "1": BOLDOFF + DIMOFF + REDF, "2": BOLDOFF + DIMOFF + GREENF, "3": BOLDOFF + DIMOFF + YELLOWF,
            "4": BOLDOFF + DIMOFF + BLUEF, "5": BOLDOFF + DIMOFF + MAGENTAF, "6": BOLDOFF + DIMOFF + CYANF, "7": BOLDOFF + DIMOFF + WHITEF,

            "A": DIMOFF + BOLDON + BLACKF, "B": DIMOFF + BOLDON + REDF, "C": DIMOFF + BOLDON + GREENF, "D": DIMOFF + BOLDON + YELLOWF,
            "E": DIMOFF + BOLDON + BLUEF, "F": DIMOFF + BOLDON + MAGENTAF, "G": DIMOFF + BOLDON + CYANF, "H": DIMOFF + BOLDON + WHITEF,

            "a": BOLDOFF + DIMON + BLACKF, "b": BOLDOFF + DIMON + REDF, "c": BOLDOFF + DIMON + GREENF, "d": BOLDOFF + DIMON + YELLOWF,
            "e": BOLDOFF + DIMON + BLUEF, "f": BOLDOFF + DIMON + MAGENTAF, "g": BOLDOFF + DIMON + CYANF, "h": BOLDOFF + DIMON + WHITEF}


bgColors = {"0": BLACKB, "1": REDB, "2": GREENB, "3": YELLOWB,
            "4": BLUEB, "5": MAGENTAB, "6": CYANB, "7": WHITEB}

def combineCodes(*ansiCodes):
    """Combines multiple ANSI excape codes

>>> combineCodes(BOLDON, REDF)
'\\x1b[1;31m'
>>> combineCodes(BOLDON, REDF, BLUEB)
'\\x1b[1;31;44m'
>>> combineCodes(BOLDON, REDF, BLUEB, "bacon")
Traceback (most recent call last):
  ...
ValueError: 'bacon' is not an ANSI code"""

    ret = ANSISTART + "{}" + ANSIEND

    retCodes = []

    for i in ansiCodes:

        if not (i.startswith(ANSISTART) and i.endswith(ANSIEND) ):
            raise ValueError("{!r} is not an ANSI code".format(i) )

        j = i.lstrip(ANSISTART)
        j = j.rstrip(ANSIEND)

        retCodes.append(j)

    retStr = ";".join(retCodes)

    return ret.format(retStr)

def stripCodes(message):

    ret = []
    removing = False

    for n, c in enumerate(message):

        if not removing:
            for n2, c2 in enumerate(ANSISTART):
                cut = n + n2

                if message[cut:cut+1] != c2:
                    break

            else:
                removing = True

            if not removing:
                ret.append(c)

        else:

            for n2, c2 in enumerate(ANSIEND):
                cut = n - n2

                if cut < 0:
                    break

                if message[cut:cut+1] != ANSIEND[-n2 - 1]:
                    break

                removing = False

    return "".join(ret)

def mapColors(strn, fgMap, bgMap=None, *, fCols=None, bCols=None):
    """Maps ANSI color codes to a string or list of strings

>>> mapColors("Potato", "AA11AA", "------")
'\\x1b[1m\\x1b[30mPo\\x1b[22m\\x1b[31mta\\x1b[1m\\x1b[30mto\\x1b[0m'
>>> print(_)
Potato


By default, the colors are:

0 - Black   fore/background
1 - Red     fore/background
2 - Green   fore/background
3 - Yellow  fore/background
4 - Blue    fore/background
5 - Magenta fore/background
6 - Cyan    fore/background
7 - White   fore/background

A - Bold black foreground
B - Bold red foreground
C - Bold green foreground
D - Bold yellow foreground
E - Bold blue foreground
F - Bold magenta foreground
G - Bold cyan foreground
H - Bold white foreground

a - Dim black foreground
b - Dim red foreground
c - Dim green foreground
d - Dim yellow foreground
e - Dim blue foreground
f - Dim magenta foreground
g - Dim cyan foreground
h - Dim white foreground"""

    if fCols is None:
        fCols = fgColors

    if bCols is None:
        bCols = bgColors

    currentColorF = ""
    currentColorB = ""

    resetF = combineCodes(DEFAULTF, BOLDOFF, DIMOFF)
    resetB = DEFAULTB

    ret = []

    if bgMap is None:
        bgMap = "-" * len(fgMap)

    if not (len(strn) == len(fgMap) == len(bgMap) ):
        raise AssertionError("string and maps not equal lengths")


    for pos, char in enumerate(strn):
        fChar = fgMap[pos]
        bChar = bgMap[pos]

        if fChar in fCols and fChar != "-":
            if currentColorF != fChar:
                ret.append(fCols[fChar] )
                currentColorF = fChar

        else:
            if currentColorF != "":
                ret.append(resetF)
            currentColorF = ""

        if bChar in bCols and bChar != "-":
            if currentColorB != bChar:
                ret.append(bCols[bChar] )
                currentColorB = bChar

        else:
            if currentColorB != "":
                ret.append(resetB)
            currentColorB = ""


        ret.append(char)

    ret.append(RESET)

    return "".join(ret)
