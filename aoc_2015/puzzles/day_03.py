from itertools import accumulate
from operator import itemgetter


def get_input():
    with open('../input/day_03.txt') as f:
        return f.readline()


def main():
    prog, dirs = get_input(), {'^': 1j, 'v': -1j, '>': 1, '<': -1}
    print(pt1 := len(set(accumulate(prog, lambda a, b: a + dirs[b], initial=0))))
    print(pt2 := len(set(map(itemgetter(0), accumulate(prog, lambda a, b: (a[1] + dirs[b], a[0]), initial=(0, 0))))))


if __name__ == '__main__':
    main()
