import re
from dataclasses import dataclass
from itertools import product, combinations

from more_itertools.more import collapse


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armour: int

    def __post_init__(self):
        self.cost = int(self.cost)
        self.damage = int(self.damage)
        self.armour = int(self.armour)

    def __add__(self, other):
        return Item(
            self.name + other.name,
            self.cost + other.cost,
            self.damage + other.damage,
            self.armour + other.armour
        )


@dataclass
class Player:
    hp: int
    items: list[Item]

    def __post_init__(self):
        self.hp = int(self.hp)

    def equip(self, item: Item):
        self.items.append(item)

    def defeats(self, other):
        return self.turns(other) >= other.turns(self)

    def turns(self, other):
        damage_per_turn = max(1, other.damage - self.armour)
        turns, remaining = divmod(self.hp, damage_per_turn)
        return turns if remaining else turns - 1

    @property
    def damage(self):
        return sum(i.damage for i in self.items)

    @property
    def armour(self):
        return sum(i.armour for i in self.items)

    @property
    def cost(self):
        return sum(i.cost for i in self.items)


def get_input():
    with open('../input/day_21.txt') as f:
        blocks = f.read().split('\n\n')
        weapons, armour, rings = map(lambda x: [Item(*l.rsplit(maxsplit=3)) for l in x.splitlines()[1:]], blocks[:3])
        enemy = (lambda hp, damage, armour: Player(hp, [Item('Base', 0, damage, armour)]))(
            *re.findall(r'\d+', blocks[3]))
        return weapons, armour, rings, enemy


def combos_in_range(iterable, start, stop):
    for i in range(start, stop + 1):
        yield from combinations(iterable, i)


def main():
    weapons, armour, rings, enemy = get_input()

    combos = product(
        combos_in_range(weapons, 1, 1),
        combos_in_range(armour, 0, 1),
        combos_in_range(rings, 0, 2)
    )

    winners = []

    for c in combos:
        p = Player(100, [])
        for i in collapse(c):
            p.equip(i)
        if p.defeats(enemy):
            winners.append(p)

    cheapest = min(winners, key=lambda k: k.cost)
    print(pt1 := cheapest.cost)

    combos = product(
        combos_in_range(weapons, 1, 1),
        combos_in_range(armour, 0, 1),
        combos_in_range(rings, 0, 2)
    )

    losers = []

    for c in combos:
        p = Player(100, [])
        for i in collapse(c):
            p.equip(i)
        if not p.defeats(enemy):
            losers.append(p)

    costliest = max(losers, key=lambda k: k.cost)
    print(pt2 := costliest.cost)


if __name__ == '__main__':
    main()
