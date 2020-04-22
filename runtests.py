#!/usr/bin/env python
import argparse
import ast
import importlib
import os
import subprocess
import sys

import pytest

STUBS_ROOT = os.path.dirname(os.path.abspath(__file__))

# Technically "public" functions (they don't start with an underscore)
# that we don't want to include.
BLACKLIST = {
    "numpy": {
        # Stdlib modules in the namespace by accident
        "absolute_import",
        "warnings",
        # Accidentally public
        "add_docstring",
        "add_newdoc",
        "add_newdoc_ufunc",
        # Builtins
        "bool",
        "complex",
        "float",
        "int",
        "long",
        "object",
        "str",
        "unicode",
        # Should use numpy_financial instead
        "fv",
        "ipmt",
        "irr",
        "mirr",
        "nper",
        "npv",
        "pmt",
        "ppmt",
        "pv",
        "rate",
    }
}


class FindAttributes(ast.NodeVisitor):
    """Find top-level attributes/functions/classes in the stubs.

    Do this by walking the stubs ast. See e.g.

    https://greentreesnakes.readthedocs.io/en/latest/index.html

    for more information on working with Python's ast.

    """

    def __init__(self):
        self.attributes = set()

    def visit_FunctionDef(self, node):
        if node.name == "__getattr__":
            # Not really a module member.
            return
        self.attributes.add(node.name)
        # Do not call self.generic_visit; we are only interested in
        # top-level functions.
        return

    def visit_ClassDef(self, node):
        if not node.name.startswith("_"):
            self.attributes.add(node.name)
        return

    def visit_AnnAssign(self, node):
        self.attributes.add(node.target.id)


def find_missing(module_name):
    module_path = os.path.join(
        STUBS_ROOT,
        module_name.replace("numpy", "numpy-stubs").replace(".", os.sep),
        "__init__.pyi",
    )

    module = importlib.import_module(module_name)
    module_attributes = {
        attribute for attribute in dir(module) if not attribute.startswith("_")
    }

    if os.path.isfile(module_path):
        with open(module_path) as f:
            tree = ast.parse(f.read())
        ast_visitor = FindAttributes()
        ast_visitor.visit(tree)
        stubs_attributes = ast_visitor.attributes
    else:
        # No stubs for this module yet.
        stubs_attributes = set()

    blacklist = BLACKLIST.get(module_name, set())

    missing = module_attributes - stubs_attributes - blacklist
    print("\n".join(sorted(missing)))


def run_pytest(argv):
    subprocess.run(
        [sys.executable, "-m", "pip", "install", STUBS_ROOT],
        capture_output=True,
        check=True,
    )
    return pytest.main([STUBS_ROOT] + argv)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--find-missing")
    args, remaining_argv = parser.parse_known_args()

    if args.find_missing is not None:
        find_missing(args.find_missing)
        sys.exit(0)

    sys.exit(run_pytest(remaining_argv))


if __name__ == "__main__":
    main()
