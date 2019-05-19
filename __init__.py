#!/usr/bin/python3

import typing as _typing;

# function types
_num2letter_fType = _typing.NewType(
    'num2letter_fType',
    _typing.Callable[[int], str]);

# modules as names
from . import english;
from . import chinese;


# functions as names
num2letter_ENG: _num2letter_fType = english.num2letter;
num2letter_CHN: _num2letter_fType = chinese.num2letter;

def _funcFromLanCode(code: str) -> _num2letter_fType:
    'returns the function if success; otherwise thrown by eval'
    head: str = 'num2letter_';
    return eval(head + code);

def interactive(
    lanCode: _typing.Optional[str] = None,
    num: _typing.Optional[int] = None,
    output: str = 'out.txt') -> None:
    '''
        the interactive function for using the program
        if output = '-', print to stdout
            if file is named literally '-',
            use './-' or '.\\-' depending on the OS
    '''
    # get function from language code
    if None == lanCode:
        lanCode = input('language code: [eng, chn]')[:3];
    num2letter_func: _num2letter_fType = _funcFromLanCode(lanCode.upper());
    # get number
    if None == num:
        while True:
            try:
                num = int(input('number (less than 100,000,000): '));
                break;
            except:
                continue;
    # have function and number
    res: str = num2letter_func(num);
    if '-' == output:
        print(res);
        return;

    with open(output, 'a', encoding = 'utf8') as f:
        print('Writing to file: ' + output);
        f.write(res);

    return;

def debug(x: _typing.Optional[int]) -> None:
    return interactive('chn', x, '-');
