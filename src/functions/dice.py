#!/usr/bin/env python3

# NOTE: I created this a very long time ago - this is not how I code
#       anymore. Please don't think I do.

import sys, random

class InvalidDieNumber(Exception): pass

def main(dieRaw):

    ret = []
    dieList = []

    for i in dieRaw:
        try:
            for j in i:
                if j not in '0123456789d*':
                    raise InvalidDieNumber
            i = i.split('*')
            i[0] = i[0].split('d')
            i[0] = [int(j) for j in i[0]]
            if len(i) == 1:
                i += [1]
            else:
                i[1] = int(i[1])
            dieList += [i]
        except InvalidDieNumber:
            pass

    totalDieSum = 0

    for dies in dieList:
        dieStr = '%id%i*%i' % (dies[0][0], dies[0][1], dies[1])
        dieSum = 0
        for die in range(dies[0][0]):
            dieSum += random.randrange(dies[0][1])+1
        dieSum *= dies[1]
        totalDieSum += dieSum

        ret.append("{}->{}".format(dieStr, dieSum))

    if len(dieRaw) > 1:
        ret.append("total - {}".format(totalDieSum))

    return " :: ".join(ret)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dieRaw = sys.argv[1:]
    else:
        print('fail')
        sys.exit()
