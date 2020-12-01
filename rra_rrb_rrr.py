def ft_rev_list(mass):
    for i in range(len(mass) - 1, -1, -1):
        mass.append(mass.pop(i))
    return mass


def rra(mass):
    a = mass.pop()
    mass = ft_rev_list(mass)
    mass.append(a)
    mass = ft_rev_list(mass)


def rrb(mass):
    b = mass.pop()
    mass = ft_rev_list(mass)
    mass.append(b)
    mass = ft_rev_list(mass)


def rrr(a, b):
    rra(a)
    rrb(b)