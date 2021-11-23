from itertools import chain
from json import loads
from re import findall


def values(obj):
    if isinstance(obj, dict):
        yield from chain.from_iterable(map(values, obj.values())) if 'red' not in obj.values() else ()
    elif isinstance(obj, list):
        yield from chain.from_iterable(map(values, obj))
    else:
        yield obj


def main():
    with open('../input/day_12.txt') as f:
        json = f.read()

    print(pt1 := sum(map(int, findall(r'(-?\d+)', json))))
    print(pt2 := sum(v for v in values(loads(json)) if isinstance(v, int)))


if __name__ == '__main__':
    main()
