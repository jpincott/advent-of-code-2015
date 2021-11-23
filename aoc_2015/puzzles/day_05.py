import re


def get_input():
    with open('../input/day_05.txt') as f:
        return f.readlines()


def main():
    words = get_input()

    # pt 1
    has_at_least_three_vowels = lambda s: sum(c in 'aeiou' for c in s) >= 3
    has_double_letter = lambda s: bool(re.search(r'(.)\1', s))
    no_banned_pairs = lambda s: not re.search(r'(ab|cd|pq|xy)', s)
    print(sum(has_at_least_three_vowels(w) and has_double_letter(w) and no_banned_pairs(w) for w in words))

    # pt 2
    has_distinct_pairs = lambda s: bool(re.search(r'(..).*\1', s))
    has_split_pair = lambda s: bool(re.search(r'(.).\1', s))
    print(sum(has_distinct_pairs(w) and has_split_pair(w) for w in words))


if __name__ == '__main__':
    main()
