from functools import cache
from itertools import count, accumulate, cycle, takewhile
from operator import add, sub

from more_itertools.more import interleave

from aoc_2015.utils.contextmanagers import timer


def gen_pen():
    return accumulate(interleave(count(1), count(3, step=2)), add, initial=1)


@cache
def sum_divs(n):
    if n <= 0:
        raise ValueError

    ops = cycle([add, add, sub, sub])
    nums = gen_pen()

    terms = list(zip(ops, takewhile(lambda t: t <= n, nums)))
    terms = list(reversed(terms))

    s = 0
    for op, num in terms:
        s = op(s, sum_divs(n - num) if n > num else n)
    return s


def main():
    with timer('pt1'):
        print(pt1 := next(n for n in count(1) if sum_divs(n) * 10 >= 33100000))


if __name__ == '__main__':
    main()
