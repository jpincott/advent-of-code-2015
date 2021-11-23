from operator import lt, eq, gt
from re import findall

from more_itertools.more import one

from aoc_2015.utils.io import stream_lines


def get_input():
    return {
        int(n): {t: int(m) for t, m in findall(r'(\w+): (\d+)', s)}
        for l in stream_lines(day=16)
        for n, s in findall(r'(\d+): (.+)', l)
    }


def get_test():
    return {t: int(m) for t, m in findall(r'(\w+): (\d+)', """
        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1
    """)}


def main():
    sues = get_input()
    test = get_test()
    print(pt1 := one(n for n, d in sues.items() if all(test[k] == v for k, v in d.items())))

    ops = {'cats': lt, 'trees': lt, 'pomeranians': gt, 'goldfish': gt}
    print(pt2 := one(n for n, d in sues.items() if all(ops.get(k, eq)(test[k], v) for k, v in d.items())))


if __name__ == '__main__':
    main()
