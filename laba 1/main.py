
'''С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным
образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное, введенное из файла

Формируется матрица F следующим образом: Скопировать в нее матрицу А и если
количество нулей в нечетных столбцах в области 4, умноженное на К больше, чем
произведение чисел в нечетных строках в области 1, то поменять симметрично области 1 и
2 местами, иначе 2 и 3 поменять местами несимметрично. При этом матрица А не
меняется. После чего вычисляется выражение: A*F+ K* F T . Выводятся по мере
формирования А, F и все матричные операции последовательно.'''

import random
def print_mat(n,mat_name):
    print("Матрица "+mat_name)
    for i in n:
        for j in i:
                print(j, end=' ')
        print()
p = 0
print("Введите K")
k = int(input())
print("Введите N")
n = int(input())
a=[[0] * n for _ in range(n)]
f=[[0] * n for _ in range(n)]
m=[[0] * n for _ in range(n)]
ft=[[0] * n for _ in range(n)]
af=[[0] * n for _ in range(n)]
kft=[[0] * n for _ in range(n)]

while p != 1:
    print("Выбор вывода матрицы: \n 1.Рандомное заполнение \n 2.Заполнение из файла")
    choice = int(input())
    if choice == 1:
        for i in range(n):
            for j in range(n):
                a[i][j]= random.randint(-10,10)
                f[i][j]=a[i][j]

        p += 1
    elif choice == 2:
        file = open("file.txt", "r")
        for i in range(n):
            stroka = file.readline().split()
            for j in range(n):
                a[i][j]=int(stroka[j])
                f[i][j]=a[i][j]

        file.close()
        p +=1
    else:
        print("Такого варианта нет в списке, выберите заново")
print_mat(a,"A")

#1область эта
s = 1
for i in range(n//2):
    for j in range(i):
        if (i % 2 == 1):
            s *= f[i][j]
for i in range(n//2, n):
    for j in range(n -(i+1)):
        if (i % 2 == 1):
            s *= f[i][j]
#тут будет 4 область
c = 0
for i in range(n):
    for j in range(i):
        if j > n - (i+1):
            if (j % 2 == 1):
                if f[i][j] == 0:
                    c += 1
c *=k
if c > s:
    for i in range(n // 2):
        for j in range(i):
            f[i][j], f[j][i] = f[j][i], f[i][j]
    for i in range(n // 2, n):
        for j in range(n - (i + 1)):
            f[i][j], f[j][i] = f[j][i],f[i][j]
else:
    for i in range(n):
        for j in range(i+1, n):
            if j < n - (i+1):
                f[i][j] , f[j][n - (i+1)] = f[j][n - (i+1)], f[i][j]
print_mat(f,"F")

for i in range(n):
    for j in range(n):
        for t in range(n):
            af[i][j] += a[i][t] * f[t][j]
print_mat(af,"AF")

for i in range(n):
    for j in range(n):
        ft[i][j] += f[j][i]
print_mat(ft,"FT")

for i in range(n):
    for j in range(n):
        kft[i][j] = k * f[i][j]
print_mat(kft,"KFT")

for i in range(n):
    for j in range(n):
        m[i][j] = af[i][j] + kft[i][j]
print_mat(m,"result")