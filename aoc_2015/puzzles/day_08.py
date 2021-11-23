def get_input():
    with open('../input/day_08.txt') as f:
        return [s.strip() for s in f.readlines()]


def main():
    strings = get_input()
    print(sum(len(s) - len(eval(s)) for s in strings))
    print(sum(2 + s.count('\\') + s.count('"') for s in strings))


if __name__ == '__main__':
    main()
