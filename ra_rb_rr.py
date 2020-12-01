def ra(mass):
    a = mass.pop(0)
    mass.append(a)


def rb(mass):
    b = mass.pop(0)
    mass.append(b)


def rr(a, b):
    ra(a)
    rb(b)

