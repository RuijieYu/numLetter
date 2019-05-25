#!/usr/bin/python3
'''
    The initialization script for numLetter.
'''

import typing as _typing;

# modules as names
from . import english;
from . import chinese;

# function types
_num2letterFType = _typing.NewType(
    'num2letterFType',
    _typing.Callable[[int], str]);

# functions as names
num2letter_ENG: _num2letterFType = english.num2letter;
num2letter_CHN: _num2letterFType = chinese.num2letter;

def _funcFromLanCode(code: str) -> _num2letterFType:
    'returns the function if success; otherwise thrown by eval'
    head: str = 'num2letter_';
    return eval(head + code);

def _allLanCodes() -> _typing.Collection[str]:
    'returns all available lanCodes'
    return ('eng', 'chn');

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
    while None is lanCode:
        print(f'[{", ".join(_allLanCodes())}]');
        lanCode = input('language code: ')[:3];
        try:
            num2letterFunc: _num2letterFType = _funcFromLanCode(lanCode.upper());
        except NameError:
            print(f'Error: bad language code <{lanCode}>');
            lanCode = None;
            continue;
    # get number
    if None is num:
        while True:
            try:
                num = int(input('number (less than 100,000,000): '));
                if num < 0:
                    raise ValueError;
                break;
            except (EOFError, ValueError) as err: # when a string cannot convert to int
                print('{0}. Try again. '.format(type(err).__name__));
                continue;
    # have function and number
    res: str = num2letterFunc(num);
    print(f'Result: {res}');
    if '-' == output:
        return;

    try:
        with open(output, 'a', encoding='utf8') as file:
            print('Appending to file: ' + output);
            file.write(res + '\n');
    except IOError:
        print(f'Error: cannot access the file "{output}". ');

    input('Press enter to continue...');
    return;

def debug(num: _typing.Optional[int]) -> None:
    'debug function'
    return interactive('chn', num, '-');
