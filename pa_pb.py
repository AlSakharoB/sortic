import split as ft4


def ft_rev_list(mass):
    a = mass[len(mass) - 1::-1]
    return a


def pa(b, a):
    if ft4.ft_len(b) > 0:
        d = b[0]
        a = ft_rev_list(a)
        a.append(d)
        a = ft_rev_list(a)
    return a


def pb(a, b):
    if ft4.ft_len(a) > 0:
        d = a[0]
        b = ft_rev_list(b)
        b.append(d)
        b = ft_rev_list(b)
    return b
