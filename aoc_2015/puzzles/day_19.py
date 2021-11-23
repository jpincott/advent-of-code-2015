import re


def get_input():
    with open('../input/day_19.txt') as f:
        subs, text = f.read().split('\n\n')
        return [sub.split(' => ') for sub in subs.splitlines()], text


def main():
    subs, text = get_input()

    def replacements(old, new, string):
        return {string[:span[0]] + new + string[span[1]:] for span in (m.span() for m in re.finditer(old, string))}

    print(pt1 := len({t for k, v in subs for t in replacements(k, v, text)}))

    def solve(string, depth=0):
        if string == 'e':
            yield depth
        else:
            for k, v in subs:
                for r in replacements(v, k, string):
                    yield from solve(r, depth + 1)

    print(pt2 := next(solve(text)))


if __name__ == '__main__':
    main()
