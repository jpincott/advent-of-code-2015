from math import prod
from operator import itemgetter

from parse import parse

from aoc_2015.utils.decorators import timer
from aoc_2015.utils.io import stream_lines


def kcom(n, p, h=()):
    yield from [(*h, n)] if p == 1 else (t for i in range(0, n - 1 + 2) for t in kcom(n - i, p - 1, (*h, i)))


def get_input():
    # Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
    return [
        parse('{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}', l).fixed
        for l in stream_lines(day=15)
    ]


@timer
def main():
    ings = get_input()

    print(pt1 := max(
        prod(
            max(0, sum(map(prod, zip(c, list(map(itemgetter(i + 1), ings))))))
            for i in range(len(c))
        )
        for c in kcom(100, 4)
    ))

    print(pt2 := max(
        prod(
            max(0, sum(map(prod, zip(c, list(map(itemgetter(i + 1), ings))))))
            for i in range(len(c))
        )
        for c in kcom(100, 4)
        if sum(map(prod, zip(c, list(map(itemgetter(-1), ings))))) == 500
    ))


if __name__ == '__main__':
    main()
