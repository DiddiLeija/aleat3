# check if using the variables "*_NAME" (from version 0.2.5 
# and added by the 'import *') are well implemented.

__author__ = "Diego Ramirez"

from aleat3 import *

# declare some variables
extras = None
d = {COIN_NAME: "aleatory.coin", 
     DICE_NAME: "aleatory.dice", 
     ROULETTE_NAME: "aleatory.roulette"}  # a dict with the variable and the meaning

for item in d.keys():
    # try with each variable
    print("Looking for '%s'..."%item)
    if item == ROULETTE_NAME:
        # add a generic list if you need a roulette
        extras = LIST_EXAMPLE
    # create 2 aleat object with the both methods
    a1 = Aleatoryous(item)
    a2 = Aleatoryous(d[item], extras=extras)
    # compare the results
    if a2.getmodetype() == a1.getmodetype():
        # this means, both types are "aleatory.coin"
        print("it is OK.")
    else:
        # i supose this won't ever happen, but it could be
        print("something is wrong with '%s'."%item)
        print(a1.getmodetype(), "!=",a2.getmodetype(), "?")
    # reset variables, if needed
    if extras is not None:
         extras = None
    del(a1, a2) # clean the aleatoryous objects

# expected output:

# $ test_2.py
# Looking for 'aleatory.coin'...
# it is OK.
# Looking for 'aleatory.dice'...
# it is OK.
# Looking for 'aleatory.roulette'...
# it is OK.
