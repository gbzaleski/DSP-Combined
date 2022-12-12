Testing
=======

Testing code is important part of write code. Properly written check if
newly written function works properly.

When using code long time there are situation where some modification of
existing function need to be introduced. Sometimes funchtions from third
party packages break backward compatybility. Existing test set allow to
fast and precise discover place in code which produce error.

There ar multiple test framework for Python. During this classes we will
focus on ``pytest``. There exist builtin python frameworks Doctest [1]_
and Unittest [2]_, but currently pytest offer better environment

Introduction
------------

One of most popular testing framework for python. To use ``pytest`` use
simple ``pytest`` or ``python -m pytest`` command in terminal.

.. code:: 

   $ pytest
   ====================================== test session starts =======================================
   platform linux -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
   rootdir: /../python-tools/testing
   collected 183 items

   code/test_conditional.py ss                                                                [  1%]
   code/test_parametrize.py ................................................................. [ 36%]
   .................................                                                          [ 54%]
   code/test_parametrize_exercise.py ........................................................ [ 85%]
   .........................                                                                  [ 98%]
   code/test_xfail.py .x                                                                      [100%]

   =========================== 180 passed, 2 skipped, 1 xfailed in 0.21s ============================

Pytest search for test function inside ``test_*.py`` or ``*_test.py``
files and collect functions with ``test_`` prefix [3]_.

.. code:: python

   from math import isclose


   def test_add():
       assert 2 + 3 == 5


   def test_div():
       assert isclose(5 / 2, 2.5)

Exercise 1
~~~~~~~~~~

Write tests for masked sum function:

.. code:: python

   def mask_sum(data, mask):
       res = 0
       for val, mask_val in zip(data, mask):
          if mask_val != 0:
               res += val
       return res

Parametrization
---------------

Fail of test function which iterate over parameters of tested function
(ex. faster implementation) inform only about one set of parameters and
need to be executed under debugger to extract problematic parameters.

Parametrize of test function is extracting such iteration outside test
function and produce clean failure information. To do it in pytest use
``pytest.mark.parametrize`` decorator.

.. code:: python

   import functools
   from typing import List

   import pytest


   @functools.lru_cache
   def fibonacci(n: int):
       """Calculate n-th fibbonaci number"""
       if n < 0:
           raise ValueError("Unsupported value")
       if n < 2:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)


   @pytest.mark.parametrize("num,res", [(0, 0), (1, 1), (2, 1), (10, 55), (18, 2584)])
   def test_fibonacci(num: int, res: int):
       assert fibonacci(num) == res


   @pytest.mark.parametrize("num", [-1, -7, -50])
   def test_fibonacci_negative(num):
       with pytest.raises(ValueError, match="Unsupported value"):
           fibonacci(num)


   def zeros_matrix(n: int, m: int) -> List[List[float]]:
       """Create n by m zeros matrix"""
       return [[0 for _ in range(m)] for _ in range(n)]


   @pytest.mark.parametrize("n_size", list(range(1, 10)))
   @pytest.mark.parametrize("m_size", list(range(1, 20, 2)))
   def test_zero_matrix(n_size, m_size):
       matrix = zeros_matrix(n_size, m_size)
       assert len(matrix) == n_size
       assert all(map(lambda x: len(x) == m_size, matrix))
       assert all([x == 0 for y in matrix for x in y])
       matrix[0][0] = 1
       assert all([x == 0 for y in matrix[1:] for x in y])
       assert all([x == 0 for x in matrix[0][1:]])

More information here:
https://docs.pytest.org/en/stable/example/parametrize.html

Exercise 2
~~~~~~~~~~

Read code from ``code/test_parametrize_exercise.py`` file. Find bug in
``norm`` function. Using ``@pytest.mark.parametrize`` modify
``test_norm`` or create a new tests function to cover missed cases.

Exercise 3
~~~~~~~~~~

Base on ``mask_sum`` from *Exercise 1* write function
``mask_aggregation`` with signature:

.. code:: python

   mask_aggregation(agg_operator: Callable[[float, float], float], data: List[float], mask: List[bool]) -> float

where ``agg_operator`` implements any associative operation (like
``operator.add``). Test it using few such operators (see
https://docs.python.org/3.4/library/operator.html) and few data points
by parametrizing test with ``pytest.mark.parametrize``

Conditional execution
---------------------

The most common source of test fail are bugs in implementation. But
tests may also fail because lack of some resources like:

-  Test data
-  Libraries
-  Operating system
-  Python version

It is better to skip such test, than get useless fail report. Test could
be skipped every time using ``pytest.mark.skip`` decorator or
``pytest.skip`` call inside test function.

If condition for function skip could be called outside test function
then ``pytest.mark.skipif`` decorator.

.. code:: python

   import csv
   import os

   import pytest

   DATA_FILE = os.path.join(
       os.path.dirname(__file__), "file_that_cannot_be_put_in_repository.csv"
   )


   def parse_file(file_path: str = DATA_FILE):
       with open(file_path) as csvfile:
           reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
           return [row for row in reader]


   @pytest.mark.skipif(not os.path.exists(DATA_FILE), reason="Missing data file")
   def test_parse_function():
       data = parse_file()
       assert len(data) == 17
       assert len(data[0]) == 11
       assert isinstance(data[0], dict)


   def test_parse_function2():
       if not os.path.exists(DATA_FILE):
           pytest.skip("Missing data file")
       data = parse_file()
       assert len(data) == 17
       assert len(data[0]) == 11
       assert isinstance(data[0], dict)

Documentation: https://docs.pytest.org/en/latest/skipping.html

Exercise 4
~~~~~~~~~~

Create test for ``math.dist`` function. Knowing that this function is
introduced in python 3.8 use ``pytest.mark.skipif`` to skip this
function test on python 3.7 and earlier.

Expected failure
----------------

There are cases where current implementation of tested function does not
satisfy specification. For example it could be caused by bug in external
package. Instead of skipping test and manually check when test starts
working there is option to mark test as expected to fail. Then if test
pass it is reported as unexpected pass. To mark test as expected to fail
use ``pytest.mark.xfail`` decorator.

.. code:: python

   import pytest


   def in_circle(x, y, radius=1):
       return x ** 2 + y ** 2 < radius ** 2


   def test_in_circle():
       assert in_circle(0, 0)
       assert in_circle(0.5, 0.5)
       assert in_circle(9, 0, 10)
       assert not in_circle(1, 1)
       assert not in_circle(100, 1, 10)


   @pytest.mark.xfail(reason="Wrong border handle")
   def test_in_circle_border():
       assert in_circle(1, 0)
       assert in_circle(0, 10, 10)

Documentation:
https://docs.pytest.org/en/latest/skipping.html#xfail-mark-test-functions-as-expected-to-fail

Fixtures
--------

   A software test fixture sets up a system for the software testing
   process by initializing it, thereby satisfying any preconditions the
   system may have. [4]_

In ``pytest`` fixtures are passed as function arguments. Its usage
allows to shorten non essential parts of test code. More interesting
builtin fixtures are

-  ``capsys`` - cap standard output and standard error output. Allow to
   check if proper information are printed
-  ``monkeypatch`` - patch only in this test. Among other things, it
   allows to set environment variables or replace some time consuming
   function with dummy one.
-  ``tmp_path`` - path to unique temporary directory. Especially useful
   when testing save operation.

Documentation: https://docs.pytest.org/en/stable/fixture.html

Capsys
~~~~~~

``capsys`` fixture provide ``readouterr`` method which return namedtuple
object with two fields ``out`` and ``err``

.. code:: python

   def test_output(capsys):
       print("hello")
       captured = capsys.readouterr()
       assert captured.out == "hello\n"

Exercise 5
^^^^^^^^^^

Using ``capsys`` fixture write test for function:

.. code:: python

   def print_info(val: int):
       if val < 0:
           print("Value need to beat least 0, not, val, file=sys.stderr)
       if val % 2 == 0:
           print(f"Value {val} is even")
       else:
           print(f"Value {val} is odd")

Monkeypatch
~~~~~~~~~~~

Official documentation:
https://docs.pytest.org/en/stable/monkeypatch.html

Documentation:
https://docs.pytest.org/en/stable/reference.html#std-fixture-monkeypatch

Exercise 6
^^^^^^^^^^

Using ``monkeypatch`` fixture for manipulate environment variables test
following function

.. code:: python

   def get_config():
       return int(os.environ.get("VERBOSITY", 0)

Exercise 7
^^^^^^^^^^

Using ``monkeypatch`` to mock ``request.get`` or ``get_courses``
function and create tests for ``calc_statistics`` from
``code/nbp_course_change/nbp_change.py``. Test should be placed in
``code/nbp_course_change/test_nbp.py``. Test should not make web
requests. NBP api description is available here: http://api.nbp.pl/

Exception test
--------------

``pytest`` support testing if an exception is raised. Bellow are few
examples:

.. code:: python

   import pytest
   from py.error import EEXIST


   def test_recreate_directory_exception(tmpdir):
       (tmpdir / "test").mkdir()
       with pytest.raises(EEXIST):
           (tmpdir / "test").mkdir()


   def test_missed_key():
       dkt = {"key": 1}
       with pytest.raises(KeyError) as execinfo:
           dkt["key2"]
       assert "'key2'" == str(execinfo.value)


   def test_list_exception():
       li = [1, 2, 3, 4, 5]
       assert li.index(2) == 1
       with pytest.raises(ValueError):
           li.index(6)
       with pytest.raises(IndexError):
           li[9]

Exercise 8
~~~~~~~~~~

Using ``pytest.raises`` write test function for different types of keys
in dictionary.

-  int
-  str
-  Tuple[int, str]
-  list
-  Tuple[list, int]

Som of them are not proper dict keys and try of its usage should be
captured by ``pytest.raises``.

.. [1]
   https://docs.python.org/3/library/doctest.html

.. [2]
   https://docs.python.org/3/library/unittest.html

.. [3]
   https://docs.pytest.org/en/stable/goodpractices.html#test-discovery

.. [4]
   https://en.wikipedia.org/wiki/Test_fixture#Software
