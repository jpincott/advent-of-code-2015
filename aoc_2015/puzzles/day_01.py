from functools import reduce
from itertools import accumulate, dropwhile


def main():
    with open('../input/day_01.txt') as f:
        print(pt1 := reduce(fn := lambda acc, x: acc + 1 if x == '(' else acc - 1, chars := f.readline(), 0))
        print(pt2 := next(dropwhile(lambda x: x[1] != -1, enumerate(accumulate(chars, fn, initial=0))))[0])


if __name__ == '__main__':
    main()
