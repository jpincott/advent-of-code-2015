from more_itertools.more import collapse
from parse import parse


def get_input():
    with open('../input/day_06.txt') as f:
        return [parse(r'{} {:d},{:d} through {:d},{:d}', l).fixed for l in f.readlines()]


def main():
    prog = get_input()

    # pt 1
    grid = [[False] * 1000 for _ in range(1000)]
    n = 0
    for ins, x0, y0, x1, y1 in prog:
        n += 1
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                grid[x][y] = True if ins == 'turn on' else False if ins == 'turn off' else not grid[x][y]
    print(sum(collapse(grid)))

    # pt 2
    grid = [[0] * 1000 for _ in range(1000)]
    n = 0
    for ins, x0, y0, x1, y1 in prog:
        n += 1
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if ins == 'turn on':
                    grid[x][y] += 1
                elif ins == 'turn off':
                    grid[x][y] = max(grid[x][y] - 1, 0)
                elif ins == 'toggle':
                    grid[x][y] += 2
    print(sum(collapse(grid)))


if __name__ == '__main__':
    main()
