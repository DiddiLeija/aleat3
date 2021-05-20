# test_1
# this test is supposed to fail, but we want
# to see HOW does it fails...

from aleat3 import Aleatoryous

try:
    # this was expected to fail
    a = Aleatoryous("aleatory.roulette", "ba ba boo")
except Exception as e:
    # print a prettier error message and give time to check it
    import time
    print("Error:", str(e))
    time.sleep(1)
a = Aleatoryous("aleatory.roulette", "ba ba boo")

# NOTE: This test file could be strongly modified on version 0.2.9. Please go
# to <http://github.com/diddileija/aleat3/issues/14> for more information.
