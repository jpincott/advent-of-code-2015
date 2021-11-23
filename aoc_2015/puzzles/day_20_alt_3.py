from numpy import zeros

from aoc_2015.utils.contextmanagers import timer as cm
from aoc_2015.utils.decorators import timer


def main():
    with cm('pt1'):
        print(p1())
    print(p2())


def p1():
    target = 33100000
    max_house = target // 10
    houses = zeros(max_house + 1)
    for e in range(1, max_house + 1):
        houses[e::e] += 10 * e
        if houses[e] >= target:
            return e


@timer
def p2():
    target = 33100000
    max_house = target // 10
    houses = zeros(max_house + 1)
    for e in range(1, max_house + 1):
        houses[e:(50 * e):e] += 11 * e
        if houses[e] >= target:
            return e


if __name__ == '__main__':
    main()
