from itertools import permutations

from more_itertools.recipes import pairwise
from networkx import Graph
from parse import parse

from aoc_2015.utils.io import stream_lines


def main():
    g = Graph()
    g.add_weighted_edges_from(parse('{} to {} = {:d}', l) for l in stream_lines(day='09'))
    print(pt1 := min(sum(g.edges[e]['weight'] for e in pairwise(p)) for p in permutations(g.nodes)))
    print(pt2 := max(sum(g.edges[e]['weight'] for e in pairwise(p)) for p in permutations(g.nodes)))


if __name__ == '__main__':
    main()
