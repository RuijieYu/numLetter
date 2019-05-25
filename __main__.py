#!python3
''

from . import interactive;

_debug: bool = True;

def debug() -> None:
    'debug function'
    interactive();


def main() -> None:
    'main function'
    interactive();

(debug if _debug else main)();
