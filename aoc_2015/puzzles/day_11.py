import re


def increment(txt, idx=7):
    carry, c = divmod(1 + ord(txt[idx]) - ord('a'), 26)
    txt = txt[:idx] + chr(ord('a') + c) + txt[idx + 1:]
    return txt if not carry else increment(txt, idx - 1)


def has_run(txt):
    return any('abcdefghijklmnopqrstuvwxyz'[i:i + 3] in txt for i in range(24))


def has_no_bad(txt):
    return all(s not in txt for s in 'iol')


def has_distinct_pairs(txt):
    return len(set(re.findall(r'(.)\1', txt))) > 1


def main():
    txt = 'hepxcrrq'
    while True:
        txt = increment(txt)
        if has_no_bad(txt) and has_distinct_pairs(txt) and has_run(txt):
            break
    print(txt)

    while True:
        txt = increment(txt)
        if has_no_bad(txt) and has_distinct_pairs(txt) and has_run(txt):
            break
    print(txt)


if __name__ == '__main__':
    main()
