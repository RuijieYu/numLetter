#!/usr/bin/python3

import typing;

_digitTuple: typing.Tuple[str] = (
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
);
def _digit(n: int, pronounceZero: bool = False) -> str:
    'converts a single digit n into its corresponding word; if pZ is false, when n=0, returns empty string'
    assert 0 <= n < 10, 'n needs to be one digit';
    return '' if n == 0 and not pronounceZero else _digitTuple[n];

_teensTuple: typing.Tuple[str] = (
    'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
);
def _teens(n: int) -> str:
    'converts a number 10 < n < 20 into its corresponding word'
    assert 10 < n < 20, 'n needs to be between (not including) 10 and 20';
    return _teensTuple[n - 11];

_tensTuple: typing.Tuple[str] = (
    '', 'ten', 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
);
def _tens(n: int) -> str:
    'converts a number n=10x into its corresponding word'
    assert 0 == n % 10, 'n needs to be divisible by 10';
    return _tensTuple[n // 10];

def _hundreds(n: int) -> str:
    'converts a number n = 100x into its corresponding phrase'
    assert 0 == n % 100, 'n needs to be divisible by 100';
    assert n > 0, 'n needs to be greater than 0';
    # in English, always use "two hundred"
    return _digit(n // 100) + ' hundred';

def _thousands(n: int) -> str:
    'converts a number n = 1000x into its corresponding phrase'
    assert 0 == n % 1000, 'n needs to be divisible by 1000';
    assert n > 0, 'n needs to be greater than 0';
    # in English, always use "two thousand"
    return _digit(n // 1000) + ' thousand';

def num2letter(n: int) -> str:
    'converts number n into its corresponding word; assuming n < 10000'
    # nine thousand nine hundred and ninty nine
    if n < 10:
        return _digit(n, True);
    elif 10 < n < 20:
        return _teens(n);
    elif n < 100:
        # forty; forty-two; ten
        tens: str = _tens(n // 10 * 10);
        digit: str = _digit(n % 10);
        return tens + ('' if not digit else '-' + digit);
    elif n < 1000:
        # five hundred
        # five hundred and [forty-two]
        hundreds: str = _hundreds(n // 100 * 100);
        remain: str = num2letter(n % 100);
        return hundreds + ('' if remain == num2letter(0) else ' and ' + remain);
    elif n < 10000:
        # four thousand three hundred and twenty-one
        # four thousand and twenty-one (when hundred == 0)
        thousands: str = _thousands(n // 1000 * 1000);
        remain: str = num2letter(n % 1000);
        return thousands + (
            # if no tail
            '' if remain == num2letter(0) else
            # if no hundred
            (' ' if 0 != (n % 1000 // 100) else ' and ') + remain
        );
    else:
        return '';
