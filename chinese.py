#!/usr/bin/python3

import typing;

_digitTuple: typing.Tuple[str] = (
    '零', '壹', '贰', '叁', '肆',
    '伍', '陆', '柒', '捌', '玖'
);
def _digit(n: int, pronounceZero: bool = True) -> str:
    'converts a single digit n into its corresponding word'
    assert 0 <= n < 10, 'n needs to be one digit';
    return '' if n == 0 and not pronounceZero else _digitTuple[n];

def _digitAt(n: int, i: int) -> int:
    'returns the i-th (r-to-l) digit of n, i >= 0, n >= 0'
    assert n >= 0 and i >= 0, 'bad input';
    return (n % (10 ** (i + 1))) // (10 ** i);

_addlTuple: typing.Tuple[str] = (
    '拾', '佰', '仟', '萬', '亿'
);
def _thousands(n: int) -> str:
    'converts number n into corresponding word, assuming n < 1e4'
    if n < 10:
        return _digit(n);
    if n < 100:
        return _digit(n // 10) + _addlTuple[0] + _digit(n % 10, False);
    if n < 1000:
        # if digit 1 is 0, needs spacer
        _spacer: str = '' if _digitAt(n, 1) else _digit(0);
        return (
            # 一百二十
            #
            # hundreds
            _digit(_digitAt(n, 2)) + _addlTuple[1] +
            # 200, 300
            ('' if 0 == n % 100 else
            # tens or spacer
            ((_spacer if _spacer else _digit(_digitAt(n, 1)) + _addlTuple[0]) +
            # ones
            _digit(_digitAt(n, 0), False)))
        );
    if n < 10000:
        if 0 == n % 1000: # 8000
            return _digit(_digitAt(n, 3)) + _addlTuple[2];
        return (
            _thousands(n // 1000 * 1000) +
            # spacer
            ('' if _digitAt(n, 2) else _digit(0)) +
            # tail
            _thousands(n % 1000)
        );
    return '';

def _hunMils(n: int) -> str:
    'converts number n into corresponding word, assuming n < 1e8'
    if n < 10000:
        return _thousands(n);
    return (
        # higher digits
        (_thousands(n // 10000) + _addlTuple[3]) +
        # spacer
        ('' if _digitAt(n, 3) else _digit(0)) +
        # lower digits
        (_thousands(n % 10000))
    );

def num2letter(n: int) -> str:
    'converts number n into its corresponding word; assuming n < 1e8'
    # 四万三千二百一十六
    # 四万零三百一十六
    # 四十万
    #
    assert n < 1e8, 'bad input for n'
    return _hunMils(int(n));
