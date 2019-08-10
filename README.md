# actionator
Python library that can monitor a series of concurrent actions and report relevant statistics

### Requirements
Python 3 installed

See installation [instructions](https://www.python.org/downloads/)

Confirm that you have at least Python >= 3.x

Ex.
```
$ python3 --version
Python 3.7.4
```

### Usage
You can see an example of how to use the actionator in a multi-threaded environment
in [sample_multithreading.py](https://github.com/interviewzz/actionator/blob/master/sample_multithreading.py)

```
$ python3 sample_multithreading.py
Expect the average time for the action jump to be 50
[{"action": "jump", "avg": 50.0}]
```

### Tests
Run unit tests for the actionator

```
$ python3 test_actionator.py
```

Ex. Passing Tests
```
$ python3 test_actionator.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.005s

OK
```
