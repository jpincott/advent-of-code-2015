from re import findall

from more_itertools.more import iterate, nth_or_last


def main():
    inp = '1113122113'
    print(len(pt1 := nth_or_last(iterate(look_and_say, inp), 40)))
    print(len(pt2 := nth_or_last(iterate(look_and_say, inp), 50)))


def look_and_say(n):
    return "".join(f"{len(g)}{c}" for g, c in findall(r'((.)\2*)', n))


if __name__ == '__main__':
    main()
