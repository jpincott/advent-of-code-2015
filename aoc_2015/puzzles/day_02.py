from itertools import starmap
from re import findall


def main():
    with open('../input/day_02.txt') as f:
        dims = [sorted(map(int, findall(r'(\d+)', l))) for l in f.readlines()]
        print(pt1 := sum(starmap(lambda x, y, z: 3 * x * y + 2 * y * z + 2 * z * x, dims)))
        print(pt2 := sum(starmap(lambda x, y, z: 2 * x + 2 * y + x * y * z, dims)))


if __name__ == '__main__':
    main()
