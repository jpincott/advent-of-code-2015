from functools import cache


def get_input():
    with open('../input/day_07.txt') as f:
        nodes = {}
        for l in f.read().splitlines():
            cmd, out = l.split(' -> ')
            cmds = cmd.split(' ')
            if len(cmds) == 1:
                inp = cmds[0]
                nodes[out] = (inp, None)
            if len(cmds) == 2:
                op, inp = cmds
                nodes[out] = ((inp,), op)
            if len(cmds) == 3:
                l, op, r = cmds
                nodes[out] = ((l, r), op)
        return nodes


@cache
def val(node):
    if node.isnumeric():
        return int(node)
    inp, op = nodes[node]
    if not op:
        return val(inp)
    else:
        return ops[op](*map(val, inp))


def main():
    global nodes
    global ops

    nodes = get_input()
    ops = {
        'NOT': lambda x: ~x % 2 ** 16,
        'OR': lambda l, r: l | r,
        'AND': lambda l, r: l & r,
        'LSHIFT': lambda l, r: l << r,
        'RSHIFT': lambda l, r: l >> r,
    }
    print(val('a'))

    val.cache_clear()
    nodes['b'] = ('3176', None)
    print(val('a'))


if __name__ == '__main__':
    main()
