import sa_sb_ss_ as ft
import pa_pb as ft1
import ra_rb_rr as ft2
import sys
import split as ft4


a = []
b = []
x = 0
n = 0
str1 = ''
fin = open("sortic_text")
fout = open("check_sortic_text", "w")
if len(sys.argv) > 1:
    a = ft4.splitoper(sys.argv[1], a)
else:
    print('Выберите способ ввода:' + '\n', '  1.Ввод строкой' + '\n', '  2.Считывание с файла')
    print('   3.Ввод до "!" знака')
    action = int(input('Способ: '))
    if action == 1:
        str1 = input('Введите числа через пробел: ')
        a = ft4.splitoper(str1, a)
    if action == 2:
        line = fin.readline()
        a = ft4.splitoper(line, a)
    if action == 3:
        print('Вводите числа через "Enter" без пробелов, чтобы закончить введите "!"')
        while x != '!':
            x = input()
            if x != '!':
                a.append(int(x))
print('Ответ программы с визуализацией:')
while len(a) > 0:
    for i in range(len(a)):
        if len(a) > 1 and int(a[0]) < int(a[1]):
            ft.sa(a)
            print('exec sa')
            print("   a -", *a)
            print("   b -", *b)
            fout.write('sa ')
        ft2.ra(a)
        print('exec ra')
        print("   a -", *a)
        print("   b -", *b)
        fout.write('ra ')
    ft1.pb(a, b)
    print('exec pb')
    print("   a -", *a)
    print("   b -", *b)
    fout.write('pb ')
for i in range(len(b)):
    ft1.pa(b, a)
    print('exec pa')
    print("   a -", *a)
    print("   b -", *b)
    fout.write('pa ')
fin.close()
fout.close()
