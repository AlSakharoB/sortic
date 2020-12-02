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
