Testing
=======

There are three main directories of tests right now:

- `pass/` which contain Python files that must pass `mypy` checking with
  no type errors
- `fail/` which contain Python files that must *fail* `mypy` checking
  with the annotated errors
- `reveal/` which contain Python files that must output the correct
  types with `reveal_type`

`fail` and `reveal` are annotated with comments that specify what error
`mypy` threw and what type should be revealed respectively. The format
looks like:

```python
bad_function   # E: <error message>
reveal_type(x)   # E: <type name>
```

Right now, the error messages and types are must be **contained within
corresponding mypy message**.

Test files that end in `_py3.py` will only be type checked against Python 3.
All other test files must be valid in both Python 2 and Python 3.

## Running the tests

To setup your test environment, cd into the root of the repo and run:


```
pip install -r test-requirements.txt
pip install .
```

Note that due to how mypy reads type information in PEP 561 packages, you'll 
need to re-run the `pip install .` command each time you change the stubs.

We use `py.test` to orchestrate our tests. You can just run:

```
py.test
```

to run the entire test suite. To run `mypy` on a specific file (which
can be useful for debugging), you can also run:

```
mypy <file_path>
```

Note that it is assumed that all of these commands target the same 
underlying Python interpreter. To ensure you're using the intended version of
Python you can use `python -m` versions of these commands instead:

```
python -m pip install -r test-requirements.txt
python -m pip install .
python -m pytest
python -m mypy <file_path>
```
