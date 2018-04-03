import os

import pytest
from mypy import api

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PASS_DIR = os.path.join(os.path.dirname(__file__), "pass")
FAIL_DIR = os.path.join(os.path.dirname(__file__), "fail")
REVEAL_DIR = os.path.join(os.path.dirname(__file__), "reveal")

os.environ['MYPYPATH'] = ROOT_DIR


def get_test_cases(directory):
    for root, __, files in os.walk(directory):
        for fname in files:
            if os.path.splitext(fname)[-1] == ".py":
                # yield relative path for nice py.test name
                yield os.path.relpath(
                    os.path.join(root, fname), start=directory)


@pytest.mark.parametrize("path", get_test_cases(PASS_DIR))
def test_success(path):
    stdout, stderr, exitcode = api.run([os.path.join(PASS_DIR, path)])
    assert stdout == ''
    assert exitcode == 0


@pytest.mark.parametrize("path", get_test_cases(FAIL_DIR))
def test_fail(path):
    stdout, stderr, exitcode = api.run([os.path.join(FAIL_DIR, path)])

    assert exitcode != 0

    with open(os.path.join(FAIL_DIR, path)) as fin:
        lines = fin.readlines()

    errors = {}
    for error_line in stdout.split("\n"):
        error_line = error_line.strip()
        if not error_line:
            continue

        lineno = int(error_line.split(":")[1])
        errors[lineno] = error_line

    for i, line in enumerate(lines):
        lineno = i + 1
        if " E:" not in line and lineno not in errors:
            continue

        target_line = lines[lineno - 1]
        if "# E:" in target_line:
            marker = target_line.split("# E:")[-1].strip()
            assert lineno in errors, f'Extra error "{marker}"'
            assert marker in errors[lineno]
        else:
            pytest.fail(f'Error {repr(errors[lineno])} not found')


@pytest.mark.parametrize("path", get_test_cases(REVEAL_DIR))
def test_reveal(path):
    stdout, stderr, exitcode = api.run([os.path.join(REVEAL_DIR, path)])

    with open(os.path.join(REVEAL_DIR, path)) as fin:
        lines = fin.readlines()

    for error_line in stdout.split("\n"):
        error_line = error_line.strip()
        if not error_line:
            continue

        lineno = int(error_line.split(":")[1])
        assert "Revealed type is" in error_line
        marker = lines[lineno - 1].split("# E:")[-1].strip()
        assert marker in error_line
