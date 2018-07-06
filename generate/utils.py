import os

from dataclasses import dataclass, field
from typing import List, Optional

import textwrap

STUB_DIR = os.path.abspath(os.path.join(__file__, "..", "..", "numpy-stubs"))


@dataclass(frozen=True)
class Arg:
    name: str
    ty: Optional[str] = None
    optional: bool = False

    def render(self) -> str:
        s = self.name
        if self.ty is not None:
            s += f": {self.ty}"
        if self.optional:
            s += " = ..."
        return s


@dataclass(frozen=True)
class Func:
    name: str
    return_type: str

    args: List[Arg] = field(default_factory=list)
    overload: bool = False

    def render(self, indent=0) -> str:
        s = f"def {self.name}("
        s += ", ".join(arg.render() for arg in self.args)
        s += f") -> {self.return_type}: ...\n"

        if self.overload:
            s = "@overload\n" + s
        return textwrap.indent(s, " " * indent)


SELF = Arg("self")
