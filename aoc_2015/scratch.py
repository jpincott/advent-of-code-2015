from itertools import product


def neighbours1(c):
    return {c + complex(re, im) for re in range(-1, 2) for im in range(-1, 2) if re or im}


def neighbours2(c):
    return {c + complex(re - 1, im - 1) for re in range(3) for im in range(3) if re * im != 1}


def neighbours3(c):
    return {c + complex(*z) for z in product((-1, 0, 1), repeat=2) if any(z)}


print(
    all(
        neighbours1(z) == neighbours2(z) == neighbours3(z)
        for z in (
            complex(re, im)
            for re in range(-10, 11)
            for im in range(-10, 11)
        )
    )
)
