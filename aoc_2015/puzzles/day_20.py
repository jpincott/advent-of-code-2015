from functools import cache
from itertools import count
from math import isqrt

from aoc_2015.utils.contextmanagers import timer


@cache
def divisors(n):
    for i in range(1, isqrt(n) + 1):
        j, r = divmod(n, i)
        if r == 0:
            yield i
            if i != j:
                yield j


def main():
    with timer('pt1'):
        print(pt1 := next(n for n in count(1) if sum(divisors(n)) * 10 >= 33100000))
    with timer('pt2'):
        print(pt2 := next(n for n in count(1) if sum(filter(lambda d: n // d <= 50, divisors(n))) * 11 >= 33100000))


if __name__ == '__main__':
    main()
