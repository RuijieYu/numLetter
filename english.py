#!/usr/bin/python3
'''
    The module that converts a number into its corresponding (British) English representation.
    There is currently no plan to support other (non-British) English representation.
    TODO add support to extend million/billion/trillion/...
    TODO with added support, decide the maximum representable number
    TODO add support to distinguish long and short scales
        (long: million, milliard, billion ...; short: million, billion, trillion ...)
        see https://www.languagesandnumbers.com/articles/en/long-and-short-numeric-scales/
        see https://en.wikipedia.org/wiki/Long_and_short_scales
'''

import typing;

from ._shared import digit, digitAt, _genericNum2LetterDoc;

lanCode: str = 'eng';
lanName: str = 'British English';
ceiling: int = int(1e6);

_digitTuple: typing.Tuple[str] = (
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
);
_teensTuple: typing.Tuple[str] = (
    'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
);
_tensTuple: typing.Tuple[str] = (
    '', 'ten', 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
);
_addlTuple: typing.Tuple[str] = (
    'hundred',
    'thousand',
);

def _digit(num: int, pronounceZero: bool = False) -> str:
    return digit(_digitTuple, num, pronounceZero);
_digit.__doc__ = digit.__doc__.format(lang=lanName);

def num2letter(num: int) -> str:
    ''
    if num < 1e1:
        return _digit(num, True);
    if 10 < num < 20:
        return _teensTuple[digitAt(num - 1, 0)];
    if num < 1e2:
        # forty; forty-two; ten
        return (
            # tens
            _tensTuple[digitAt(num, 1)] + (
                # spacer
                '' if not digitAt(num, 0) else '-'
                # ones
                + _digit(digitAt(num, 0))
            )
        );
    if num < 1e3:
        # five hundred; five hundred [and forty-two]
        return (
            # hundred
            '{0} {1}'.format(_digit(digitAt(num, 2)), _addlTuple[0]) + (
                # remains if exist
                '' if not num % 100 else f' and {num2letter(num % 100)}'
            )
        );
    if num < 1e6:
        # X thousand (and) X
        return (
            # X thousand
            '{0} {1}'.format(num2letter(int(num // 1e3)), _addlTuple[1]) + (
                # end if tail=0; no 'and' if hundred!=0
                '' if not int(num % 1e3) else (
                    f' {"" if digitAt(num, 2) else "and "}{num2letter(int(num % 1e3))}'
                )
            )
        );
    return '';
num2letter.__doc__ = _genericNum2LetterDoc.format(lang=lanName, max=ceiling);
