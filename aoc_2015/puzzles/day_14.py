from collections import Counter
from itertools import chain
from operator import itemgetter

from more_itertools.more import bucket
from parse import parse

from aoc_2015.utils.io import stream_lines


def get_input():
    fmt = '{name} can fly {velocity:d} km/s for {duration:d} seconds, but then must rest for {rest:d} seconds.'
    return [parse(fmt, l).named for l in stream_lines(day=14)]


def dist(time, velocity, duration, rest, **_):
    full, remaining = divmod(time, duration + rest)
    return velocity * (full * duration + min(remaining, duration))


def main():
    input = get_input()

    print(pt1 := max(
        dist(2503, **r)
        for r in input
    ))

    print(pt2 := max(
        Counter(chain.from_iterable(
            map(itemgetter('name'), (b := bucket(input, lambda r: dist(t + 1, **r)))[max(b)])
            for t in range(2503)
        )).values()
    ))


if __name__ == '__main__':
    main()
