#!/usr/bin/python3
'''
    The module that converts a number into its corresponding (formal) Chinese representation.
    TODO provide option to switch between formal and informal representation.
'''

import typing;

from ._shared import digit, digitAt, _genericNum2LetterDoc;

lanCode: str = 'chn';
lanName: str = 'Chinese';
ceiling: int = int(1e8);

_digitTuple: typing.Tuple[str] = (
    '零', '壹', '贰', '叁', '肆',
    '伍', '陆', '柒', '捌', '玖'
);

def _digit(num: int, pronounceZero: bool = True) -> str:
    return digit(_digitTuple, num, pronounceZero);
_digit.__doc__ = digit.__doc__.format(lang='Chinese');

_addlTuple: typing.Tuple[str] = (
    '拾', '佰', '仟', '萬', '亿'
);
def _thousands(num: int) -> str:
    'converts number n into corresponding word, assuming n < 1e4'
    if num < 10:
        return _digit(num);
    if num < 100:
        return _digit(num // 10) + _addlTuple[0] + _digit(num % 10, False);
    if num < 1000:
        # if digit 1 is 0, needs spacer
        _spacer: str = '' if digitAt(num, 1) else _digit(0);
        return (
            # 一百二十
            #
            # hundreds
            _digit(digitAt(num, 2)) + _addlTuple[1] +
            # 200, 300
            ('' if 0 == num % 100 else
             # tens or spacer
             ((_spacer if _spacer else _digit(digitAt(num, 1)) + _addlTuple[0]) +
              # ones
              _digit(digitAt(num, 0), False)))
        );
    if num < 10000:
        if 0 == num % 1000: # 8000
            return _digit(digitAt(num, 3)) + _addlTuple[2];
        return (
            _thousands(num // 1000 * 1000) +
            # spacer
            ('' if digitAt(num, 2) else _digit(0)) +
            # tail
            _thousands(num % 1000)
        );
    return '';

def _hunMils(num: int) -> str:
    'converts number n into corresponding word, assuming n < 1e8'
    if num < 10000:
        return _thousands(num);
    return (
        # higher digits
        (_thousands(num // 10000) + _addlTuple[3]) +
        # spacer
        ('' if digitAt(num, 3) else _digit(0)) +
        # lower digits
        (_thousands(num % 10000))
    );

def num2letter(num: int) -> str:
    ''
    # 四万三千二百一十六
    # 四万零三百一十六
    # 四十万
    #
    assert num < 1e8, 'bad input for n'
    return _hunMils(int(num));
num2letter.__doc__ = _genericNum2LetterDoc.format(lang=lanCode, max=ceiling);
