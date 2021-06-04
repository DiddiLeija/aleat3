# Release notes for aleat3

### What's new in aleat3 0.3.0

- Bug fixes
  - Internal operation fixes
- Documentation restructuring
  - Some contents were moved
- Trivial fixes
  - `__author__` is now on `aleat3.__init__` (not `aleat3.constructor`)
  - The `aleat3.output.init_errors` will no longer support module tests, according to PR [\#28](http://github.com/diddileija/aleat3/pull/28)

### What's new in aleat3 0.2.9

- Bug fixes
- Documentation fixes

### What's new in aleat3 0.2.8

- Bug fixes
  - Improved error handling

### What's new in aleat3 0.2.7

- The `aleat3.fixme` folder has been deleted according to the issue [\#5](http://github.com/diddileija/aleat3/issues/5)

### What's new in aleat3 0.2.6

- Minor bug fixes
  - Constructor (`__init__`) issues solved.

### What's new in aleat3 0.2.5

- Special progress: we are now on [GitHub](http://github.com/diddileija/aleat3)!
  - This change came with even more changes:
    - There are Markdown documents (like this one!)
    - New 'tests' folder.
- The object `aleat3.Aleatoryous` has changes.
  - For the `extras` parameter, it also accepts tuples.

### What's new in aleat3 0.2.4

- The aleat3 scripts have been deleted.
- New features
  - New `Aleatoryous()` mode option: `"random"`. __Check documentation to learn more.__
  - New variable: `LIST_EXAMPLE`

### What's new in aleat3 0.2.3

- Minor bug fixes
  - Variable minor fixes

### What's new in aleat3 0.2.2

- The aleat3 scripts has changes. __Check documentation to learn about this fixes.__

### What's new in aleat3 0.2.1

- Minor bug fixes
  - Some variable fixes

### What's new in aleat3 0.2

- New `setup()` feature: [console_scripts](https://packaging.python.org/guides/distributing-packages-using-setuptools/#console-scripts).
  - View documentation, at section "aleat3 scripts".
- Some variable fixes

### What's new in aleat3 versions 0.1.6 up to 0.1.9

- 'Applications' library fixes
  - `CoinWinners.py` fixed
- Code bug fixes
  - Get the `__version__` and the `__author__` data easier.

### What's new in aleat3 0.1.5

- Minor bug fixes
  - Less repetitions at code.
  - 'Applications' library corrected
- New colored output
  - More [Colorama](http://pypi.org/project/colorama) functions are used
- New 'Applications' file: `diceMove.py`
  - Play with the computer to gain 50 points with `aleatory.dice`

### What's new in aleat3 0.1.4

- Minor bug fixes
  - Less repetitions at code.
  - Variable `aleat3.constructor.__version__` corrected.

### What's new in aleat3 0.1.3

- Bug fixes attempted
  - Fixed `aleat3.Aleatoryous.first_given()` method.
- New feature: __'Applications' library__.

Let's talk about this new feature. At `aleat3.applications` library you can run many
examples of Aleatoryous programming. The unable examples at this version are:

- diceInterface.py
  - Use [tkinter](http://docs.python.org/3.8/library/tkinter) library for a dice interface.
- rouletteWinners.py
  - Operate a long string of names and get 5 winners.
- coinWinners.py
  - Play with Heads or Tails and receive if you won or not.

To call this functions, import the example and just `run()` it:

```python
from aleat3.applications import rouletteWinners  # As an example
rouletteWinners.run()
```

### What's new in aleat3 0.1.2 / aleat3 0.1.2.post1

- Minor bug fixes
  - Sometimes, the `module_test()` function failed at `__main__` level.

### What's new in aleat3 0.1.1

- New developer features: Module tests
  - We are talking about `module_test()` function. View the new section _Module tests_.

### What's new in aleat3 0.0.9

- New features:
  - Some output is colored with [Colorama](http://pypi.org/project/colorama).
    - _To view this function, you must install the Colorama library at PyPi._
  - __New function: coinToBool__. View the _aleatory.coin_ section to learn more.

### Hold on... what about 0.0.8?

This version where released before, but it returned several errors. Then, version
0.0.9 is now released.

### What's new in aleat3 0.0.7

- Minor bugs resolved:
  - Sometimes, version 0.0.6 could not make the "no-repetition" operation.

### What's new in aleat3 0.0.6

- Minor bugs resolved:
  - Sometimes, version 0.0.5 did not return `__version__` output correctly.
  - Some exception handling were wrong at versions 0.0.4 and 0.0.5.
  - The operations are much cleaner and without repetitions.
- __New option at__ `Aleatoryous.first_given()`__: no-repetition.__
  - _View the "Iterating with aleatory.roulette" section_ to learn more about his feature.

### What's new in aleat3 0.0.5

- Some variables deleted or recycled:
  - Private variables recycled

### What's new in aleat3 0.0.4

- Minor bugs resolved:
  - Cleaner output
  - Faster operations
- Some variables deleted or recycled:
  - Variable `Aleatoryous.cache` deleted
  - Variable `Aleatoryous.it` deleted
  - Private variables recycled

### What's new in aleat3 0.0.3

At version 0.0.2, you could change the Aleatoryous mode by typing:

```python
obj = Aleatoryous("aleatory.coin")

obj.mode = "Dice"
```

But now, **that operation is forbidden**, and the system might return a message
like this:

```
Traceback (most recent call last):
File .../-.py in <module>
    obj.mode = "Dice"
        ^
AttributeError: object "Aleatoryous" has no attribute "mode"
```

Instead of that, **use the new method _Aleatoryous.changemode()_**:

```python
obj.changemode("aleatory.dice")
```

Also, in version 0.0.3, you can get the mode name of your object:

```python
print(obj.getmode())
```
