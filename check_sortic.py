import sa_sb_ss_ as ft
import pa_pb as ft1
import ra_rb_rr as ft2
import rra_rrb_rrr as ft3
import sys
import split as ft4
import cut as ft5


b = []
a = []
c = []
f = []
oper_line = []
oper = ''
str1 = ''
str2 = ''
x = 0
fin1 = open("sortic_text")
f = ft4.splitoper(fin1.readline(), f)
if ft4.ft_len(sys.argv) > 2:
    a = ft4.splitoper(sys.argv[1], a)
    c = ft4.splitoper(sys.argv[1], c)
    oper_line = ft4.splitoper(sys.argv[2], oper_line)
else:
    print('Выберите способ ввода:' + '\n', '  1.Ввод строкой' + '\n', '  2.Считывание с файла')
    print('   3.Ввод до "!" чисел и до "*" операций')
    action = int(input('Способ: '))
    if action == 1:
        str1 = input('Введите числа через пробел: ')
        a = ft4.splitoper(str1, a)
        c = ft4.splitoper(str1, c)
        str2 = input('Введите операции через пробел: ')
        oper_line = ft4.splitoper(str2, oper_line)
    if action == 2:
        for i in f:
            a.append(int(i))
            c.append(int(i))
        fin = open("check_sortic_text")
        oper_line = ft4.splitoper(fin.read(), oper_line)
    if action == 3:
        print('Вводите числа через "Enter" без пробелов, чтобы закончить введите "!"')
        while x != '!':
            x = input()
            if x != '!':
                a.append(int(x))
                c.append(int(x))
        print('Вводите операции через "Enter" без пробелов, чтобы закончить введите "*"')
        while oper != '*':
            oper = input()
            if oper != '*':
                oper_line.append(oper)
for i in range(ft4.ft_len(c) - 1):
    for j in range(ft4.ft_len(c) - 1 - i):
        if c[j] > c[j + 1]:
            c[j], c[j + 1] = c[j + 1], c[j]
for i in oper_line:
    if i == 'sa':
        ft.sa(a)
    if i == 'ra':
        ft2.ra(a)
        a = ft5.cut(a)
    if i == 'pa':
        a = ft1.pa(b, a)
        b = ft5.cut(b)
    if i == 'pb':
        b = ft1.pb(a, b)
        a = ft5.cut(a)
    if i == 'sb':
        ft.sb(b)
    if i == 'ss':
        ft.ss(a, b)
    if i == 'rb':
        ft2.rb(b)
        b = ft5.cut(b)
    if i == 'rr':
        ft2.rr(a, b)
        a = ft5.cut(a)
        b = ft5.cut(b)
    if i == 'rra':
        a = ft3.rra(a)
    if i == 'rrb':
        b = ft3.rrb(b)
    if i == 'rrr':
        ft3.rrr(a, b)
print(a,b,c)
print('Ответ программы:')
if ft4.ft_len(sys.argv) > 2:
    if a == c:
        print('OK')
    else:
        print('KO')
else:
    if a == c:
        print("\033[32m {}" .format("OK"))
    else:
        print("\033[31m {}" .format("KO"))
