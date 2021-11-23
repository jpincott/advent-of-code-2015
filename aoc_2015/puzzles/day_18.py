from collections import Counter
from functools import cache, reduce
from itertools import product

from aoc_2015.utils.decorators import timer
from aoc_2015.utils.io import stream_lines


def get_input():
    return {complex(x, y) for y, l in enumerate(stream_lines(day=18)) for x, c in enumerate(l.strip()) if c == '#'}


@cache
def neighbours(c):
    deltas = {complex(*d) for d in product((-1, 0, 1), repeat=2)}
    border = {c + d for d in deltas} - {c}
    return {c for c in border if all(k in range(100) for k in (c.real, c.imag))}


def evolve(cells):
    next_gen = set()
    inactive = Counter()

    # check active cells
    for c in cells:

        # get all neighbours (excludes self and is bound to X,Y grid)
        n = neighbours(c)

        # propagate to next gen if 2 or 3 active neighbours
        if len(n & cells) in (2, 3):
            next_gen.add(c)

        # increment active neighbour count (self) for all inactive neighbours
        inactive.update(n - cells)

    return next_gen | {c for c, n in inactive.items() if n == 3}


def get_fixed():
    return {complex(*p) for p in product((0, 99), repeat=2)}


@timer
def main():
    cells = get_input()
    print(pt1 := len(reduce(lambda acc, _: evolve(acc), range(100), cells)))

    fixed = get_fixed()
    print(pt2 := len(reduce(lambda acc, _: evolve(acc) | fixed, range(100), cells | fixed)))


if __name__ == '__main__':
    main()
