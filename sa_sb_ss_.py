import split as ft4


def sa(mass):
    if ft4.ft_len(mass) > 1:
        a = mass[0]
        mass[0] = mass[1]
        mass[1] = a


def sb(mass):
    if ft4.ft_len(mass) > 1:
        a = mass[0]
        mass[0] = mass[1]
        mass[1] = a


def ss(a, b):
    if ft4.ft_len(a) > 1 and ft4.ft_len(b) > 1:
        sa(a)
        sb(b)





