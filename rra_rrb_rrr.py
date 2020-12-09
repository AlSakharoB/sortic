import cut as ft5


def ft_rev_list(mass):
    a = mass[len(mass) - 1::-1]
    return a


def rra(mass):
    if len(mass) > 0:
        a = mass[len(mass) - 1]
        c = []
        c.append(a)
        for i in mass[:len(mass) - 1:]:
            c.append(i)
        return c


def rrb(mass):
    if len(mass) > 0:
        a = mass[len(mass) - 1]
        c = []
        c.append(a)
        for i in mass[:len(mass) - 1:]:
            c.append(i)
        return c


def rrr(a, b):
    a = rra(a)
    b = rrb(b)
