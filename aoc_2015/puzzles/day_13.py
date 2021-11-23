from itertools import permutations

from networkx import DiGraph
from parse import parse

from aoc_2015.utils.io import stream_lines


def get_input():
    return DiGraph(
        (a, b, {'weight': w if s == 'gain' else -w})
        for a, s, w, b in (
            parse('{} would {} {:d} happiness units by sitting next to {}.', l).fixed
            for l in stream_lines(day=13)
        )
    )


def main():
    g = get_input()
    print(pt1 := max(
        sum(g.edges[e]['weight'] + g.edges[e[::-1]]['weight'] for e in [(p[i - 1], n) for i, n in enumerate(p)])
        for p in permutations(g.nodes)
    ))

    for n in [*g.nodes]:
        g.add_weighted_edges_from([('Me', n, 0), (n, 'Me', 0)])

    print(pt2 := max(
        sum(g.edges[e]['weight'] + g.edges[e[::-1]]['weight'] for e in [(p[i - 1], n) for i, n in enumerate(p)])
        for p in permutations(g.nodes)
    ))


if __name__ == '__main__':
    main()
