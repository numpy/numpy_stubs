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

## Running the tests

We use `py.test` to orchestrate our tests. You can just run:

```
py.test
```

to run the entire test suite. To run `mypy` on a specific file (which
can be useful for debugging), you can also run:

```
$ cd tests
$ MYPYPATH=.. mypy <file_path>
```
