# test_1
# this test is supposed to fail, but we want
# to see HOW does it fails... for that, use a
# try/except block to catch the exception, print
# it in a fancy way and quit.

from aleat3 import Aleatoryous

try:
    # this was expected to fail
    a = Aleatoryous("aleatory.roulette", "a simple string")
except Exception as e:
    # print a prettier error message and give time to check it
    import time
    print("Error:", str(e))
    time.sleep(1)

# Expected output:

# $ test_1.py
# Error: ...
