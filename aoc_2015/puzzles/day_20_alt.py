from aoc_2015.utils.contextmanagers import timer as cm
from aoc_2015.utils.decorators import timer


def main():
    with cm('pt1'):
        print(p1())
    print(p2())


def p1():
    target = 33100000
    max_house = target // 10
    houses = [0] * (max_house + 1)
    for e in range(1, max_house + 1):
        for h in range(e, max_house + 1, e):
            houses[h] += 10 * e
        if houses[e] >= target:
            return e


@timer
def p2():
    target = 33100000
    max_house = target // 10
    houses = [0] * (max_house + 1)
    for e in range(1, max_house + 1):
        for h in range(e, min(50 * e, max_house) + 1, e):
            houses[h] += 11 * e
        if houses[e] >= target:
            return e


if __name__ == '__main__':
    main()
