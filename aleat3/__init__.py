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

Go to aleat3/constructor.py to check the code behind aleat3. This __init__ is only used when you import any file on the
package.
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
        print(k, "is OK")
        time.sleep(1)
