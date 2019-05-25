#!python3
'''
    The functionalities used by multiple language-specific modules
'''
import typing;
from collections import abc as cabc;

def _hasKey(collection: typing.Collection[str], key: int) -> bool:
    'returns whether the collection has desired key'
    if isinstance(collection, cabc.Mapping):
        # key based
        return key in collection;
    elif isinstance(collection, cabc.Collection):
        # assume index based
        return 0 <= key < len(collection);
    else:
        return NotImplemented;

def digit(
        digitTuple: typing.Collection[str],
        num: int, pronounceZero: bool) -> str:
    '''
        converts a single digit into its corresponding word in {lang}
        using the data from digitTuple, where
            digitTuple[i] with int i in [0, 10) must be defined
    '''
    _range: range = range(10);
    for ind in _range:
        assert _hasKey(digitTuple, ind), f'Error: index {ind} not found';
        assert isinstance(digitTuple[ind], str), f'Error: index {ind} not str';
    assert 0 <= num < 10, f'only one digit allowed for num; currently {num}';

    return '' if num == 0 and not pronounceZero else digitTuple[num];

def digitAt(num: int, i: int) -> int:
    'returns the i-th (right-to-left) digit of n, i >= 0, n >= 0'
    assert num >= 0 and i >= 0, (
        f'num and i must be nonnegative; currently {num} and {i}'
    );
    return (
        num
        # cut head
        % (10 ** (i + 1))
        # cut tail
        // (10 ** i)
    );

_genericNum2LetterDoc: str = '''
    converts num into its corresponding word in {lang};
    assuming num < {max}
''';
