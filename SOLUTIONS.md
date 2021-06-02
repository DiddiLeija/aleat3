# Building solutions with Aleatoryous - Some examples

There are several ways to applicate the aleat3 features, from math education to
game development, you can use the Aleatoryous object and other functions included
by many, many ways. We are giving some examples:

#### Making loops with _aleatory.roulette_

The most used mode is *aleatory.roulette*, because you can control data to be
iterated in aleatory selection.

For example, if you read a file `register.txt` like this:

```
John
Richard
Tamara
Axel
Gael
Sarah
Chuck
```

and you want to get a random line, use:

```python
# The file register.txt will contain many-many-many names. We want 5 aleatory
# winners:

f = open("C://Users/Admin/Documents/register.txt", "r")
l = []

for i in f:
  l.append(i.rstrip())

# Operate the file data
from aleat3 import *

r = Aleatoryous("aleatory.roulette", l)
res = r.first_given(5, repeat=False)      # New since version 0.0.6: no-repetition
print(res)
```

And we'll get an output like:

```python
["Richard", "Gael", "John", "Tamara", "Sarah"]
```

#### Binary aleatory numbers with _aleatory.coin and coinToBinary_

As we said before, the *coinToBinary* function converts an *aleatory.coin* output
to pseudo-binary numbers (1 or 0). We can use this function when you need an aleatory
output between 1 and 0. View the _Using coinToBinary function_ process shown above.

#### Building a game syntax with _aleatory.dice_

You could use the *aleatory.dice* natural properties for building complex games
where a dice is required.

For example, you can implement a GUI, and then use the *aleatory.dice* to create a game syntax where
the user will need a dice rolling.

## `aleat3.applications` examples

Use the `aleat3.applications` to view simple examples to test the aleat3 rendering.
