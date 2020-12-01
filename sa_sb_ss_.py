def sa(mass):
    if len(mass) > 1:
        a = mass[0]
        mass[0] = mass[1]
        mass[1] = a


def sb(mass):
    if len(mass) > 1:
        a = mass[0]
        mass[0] = mass[1]
        mass[1] = a


def ss(a, b):
    if len(a) > 1 and len(b) > 1:
        sa(a)
        sb(b)





