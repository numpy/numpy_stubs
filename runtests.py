#!/usr/bin/env python
import os
import subprocess
import sys

import pytest

STUBS_ROOT = os.path.dirname(os.path.abspath(__file__))


def main():
    subprocess.run(
        [sys.executable, '-m', 'pip', 'install', STUBS_ROOT],
        capture_output=True,
        check=True,
    )
    sys.exit(pytest.main([STUBS_ROOT] + sys.argv[1:]))


if __name__ == '__main__':
    main()
