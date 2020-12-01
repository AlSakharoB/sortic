def ft_rev_list(mass):
    for i in range(len(mass) - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass


def pa(b, a):
    if len(b) > 0:
        d = b.pop(0)
        a = ft_rev_list(a)
        a.append(d)
        a = ft_rev_list(a)


def pb(a, b):
    if len(a) > 0:
        d = a.pop(0)
        b = ft_rev_list(b)
        b.append(d)
        b = ft_rev_list(b)
