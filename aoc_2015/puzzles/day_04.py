from functools import partial
from hashlib import md5
from itertools import dropwhile, count


def mine(key, bits):
    return next(dropwhile(lambda n: md5(f'{key}{n}'.encode()).hexdigest()[:bits] != '0' * bits, count(0)))


def main():
    mine_bits = partial(mine, 'yzbqklnj')
    print(pt1 := mine_bits(5))
    print(pt2 := mine_bits(6))


if __name__ == '__main__':
    main()
