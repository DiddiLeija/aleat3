# Ramz Editions Copyright (c) 2020 Copyright Holder All Rights Reserved.
"New since 0.2.3: __main__ level is now safe!"
if __name__ == '__main__':
    from constructor import *
    from applications import apps
else:
    from aleat3.constructor import *
    from aleat3.applications import apps

# Alias for the object importing:
_a3 = Aleatoryous
_aleat = Aleatoryous
_ie = InitError
_a = apps
_app = _a

__author__ = "Diego Ramirez (dr01191115@gmail.com) @DiddiLeija"
__version__ = "0.2.8"


# A short guide of the Aleatoryous Object:
"""The Diddi's Aleatoryous Project.
===============================================================================================================================
INTRODUCTION

This object was created to give the folowing values:
   1. A 'dice' algorythm.
   2. A 'coin' algorythm.
   3. A 'roulette' algorythm.

In this edition we give a little guide of the posible custom methods of Aleatoryous. We also provided more objects.
===============================================================================================================================
USER GUIDE

To call this Object, type this:

>>>from aleat3 import Aleatoryous

Now, the object creation has two parameters that you should give:

>>>object = Aleatoryous("aleatory.dice", None)
                                 ^         ^
1. The 'mode'.
2. The objects (only for the 'roulette' syntax. In other cases, type None).

The method single() gets only one iteration, and can return a Value (String or Integer (In the case of the 'Dice')):

>>>coin = Aleatoryous("aleatory.coin", None)
>>>print(coin.single())
Head
>>>print(coin.single())
Head
>>>print(coin.single())
Tails

The method first_5() does the same 5 times and returns a list:

>>>dice = Aleatoryous("aleatory.dice", None)
>>>print(dice.first_5())
[6, 3, 5, 6, 1]

The methods first_5_basic() and refresh() are called internally ONLY.
The 'Roulette' syntax is more complex than the others. Look at this:

>>>roul = Aleatoryous("aleatory.roulette", ["Go to sleep",
...                                         "Play videogames",
...                                         "Play the guitar",
...                                         "Make a phone call to Castol",
...                                         "Nothing"])

But the rest is not so different:

>>>print(roul.single())
Make a phone call to Castol
>>>print(dice.first_5())
["Make a phone call to Castol", "Play videogames", "Go to sleep", "Nothing", "Make a phone call to Castol"]

The methods first_10(), first_50() and first_100() are variations of first_5(), so they work as the same:

>>>dice = Aleatoryous("aleatory.dice", None)
>>>tot = dice.first_100()
>>>print(tot[45])
4
>>>print(tot[99])
2
>>>print(tot[12:14])
[5, 1]
===============================================================================================================================
CREDITS

Created by Diego Ramirez and the Ramz Editions (c) Team. 2020 All rights reserved."""

if __name__ == '__main__':
    import time
    e = Aleatoryous()
    for k, v in {"aleatory.dice": None, "aleatory.coin": None, "aleatory.roulette": [1, 2, 3]}:
        print("Testing", k)
        d.changemode(k)
        print(d.single())
        print(k, "OK")
        time.sleep(1)
