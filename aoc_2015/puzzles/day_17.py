from collections import Counter
from itertools import chain

from aoc_2015.utils.io import stream_lines


def get_input():
    return sorted(int(n) for n in stream_lines(day=17))


def solve(target, nums, hist):
    if not target:
        yield hist
    else:
        yield from chain.from_iterable(
            solve(target - n, nums[i + 1:], hist + [n]) for i, n in enumerate(nums) if n <= target
        )


def main():
    nums = get_input()
    target = 150

    l = list(solve(target, nums, []))
    print(pt1 := len(l))

    c = Counter(len(g) for g in l)
    print(pt2 := c[min(c)])


if __name__ == '__main__':
    main()
