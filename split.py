def split(str1, mass):
    str2 = ''
    for i in str1:
        if i != ' ' and i != '\n':
            mass.append(i)
    return mass


def splitoper(str2, mass):
    str2 += ' '
    strdop = ''
    for i in str2:
        if i != ' ':
            strdop += i
        if i == ' ':
            mass.append(strdop)
            strdop = ''
    return mass
