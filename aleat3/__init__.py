# Diego Ramirez (c) 2021 Copyright Holder All Rights Reserved.
# New since 0.2.3: __main__ level is now safe!
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

# generic variables
__author__ = "Diego Ramirez (dr01191115@gmail.com) @DiddiLeija" # @DiddiLeija is from GitHub
__version__ = "0.3.0" # ignore the pre-releases / post versions tags

if __name__ == '__main__':
    import time
    e = Aleatoryous()
    for k, v in {"aleatory.dice": None, "aleatory.coin": None, "aleatory.roulette": [1, 2, 3]}:
        print("Testing", k)
        d.changemode(k)
        print(d.single())
        print(k, "is OK")
        time.sleep(1)
