import sa_sb_ss_ as ft
import pa_pb as ft1
import ra_rb_rr as ft2
import rra_rrb_rrr as ft3
import sys
import split as ft4


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
if len(sys.argv) > 2:
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
        print('Вводите числа через "Enter", чтобы закончить введите "!"')
        while x != '!':
            x = input()
            if x != '!':
                a.append(int(x))
                c.append(int(x))
        print('Вводите операции через "Enter", чтобы закончить введите "*"')
        while oper != '*':
            oper = input()
            if oper != '*':
                oper_line.append(oper)
for i in range(len(c) - 1):
    for j in range(len(c) - 1 - i):
        if c[j] > c[j + 1]:
            c[j], c[j + 1] = c[j + 1], c[j]
for i in oper_line:
    if i == 'sa':
        ft.sa(a)
    if i == 'ra':
        ft2.ra(a)
    if i == 'pa':
        ft1.pa(b, a)
    if i == 'pb':
        ft1.pb(a, b)
    if i == 'sb':
        ft.sb(b)
    if i == 'ss':
        ft.ss(a, b)
    if i == 'rb':
        ft2.rb(b)
    if i == 'rr':
        ft2.rr(a, b)
    if i == 'rra':
        ft3.rra(a)
    if i == 'rrb':
        ft3.rrb(b)
    if i == 'rrr':
        ft3.rrr(a, b)
print('Ответ программы:')
if len(sys.argv) > 2:
    if a == c:
        print('OK')
    else:
        print('KO')
else:
    if a == c:
        print("\033[32m {}" .format("OK"))
    else:
        print("\033[31m {}" .format("KO"))
