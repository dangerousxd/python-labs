
"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное (ввод из файла и генератором).
 Вид матрицы А:
В               E

С               D


На основе матрицы А формируется матрица F. По матрице F необходимо вывести не менее 3 разных графика. Программа должна использовать функции библиотек numpy и matplotlib

Формируется матрица F следующим образом:
скопировать в нее А и если в С количество чисел, больших К
в нечетных столбцах больше, чем произведение чисел в нечетных строках,
то поменять местами С и В симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А
больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F-1,
иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно."""


import numpy as np
import matplotlib.pyplot as plt

#Заполнение матриц
N, K = int(input('Введите число N: ')), int(input('Введите число K: '))
variable = 0
variable2 = 1
while variable !=1:
    print('Заполненеи матрицы: \n1.Рандомно \n2.Из файла')
    output = int(input())
    if output == 1:
        A = np.random.randint(-10, 10, size=(N, N))
        print(f'Матрица А: \n{A}')
        variable = 1
    elif output ==2:
        file = open('textfile2', 'r')
        A = np.genfromtxt('textfile2', dtype = int, usecols = range(0, N), max_rows = N)
        file.close()
        print(f'Матрица А: \n{A}')
        variable = 1
    else:
        print('Такого варианта нет, попробуйте снова.')
variable =0
F = A.copy()

#Проверка областей и замена их
for i in range(N//2,N):
    for j in range(N//2):
            if j % 2 == 1 and F[i][j] > K:
                variable +=1
            elif j % 2 == 1 :
                 variable2 *= F[i][j]
if variable > variable2:
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[N -(i+1)][j] = F[N- (i+1)][j], F[i][j]
else:
    for j in range(N//2):
        for i in range(N//2,N):
            F[i][j], F[j][i] = F[j][i], F[i][j]

print(f'Матрица F: \n{F}')
"""A * A^T – K * F^-1              (A^-1 +G-F^Т)*K"""
# Математика
opr = round(np.linalg.det(A)) # Нахождение определителя
two_diag = np.fliplr(F) # Для нахождения суммы элементов побочной диагоняли
sum_diag = np.trace(F) + np.trace(two_diag) #сумма элементов диагоналей

if opr > sum_diag:
    AT = A.transpose() #Транспонирование 1.AAT = np.dot(A,AT) - перемножение 2.linalg.matrix_power() - возведение в степень
    Itog = np.dot(A,AT) - K * np.linalg.matrix_power(F,-1) #A * A^T – K * F^-1
    print(f'Матрица Итоговая 1 вариант: \n{Itog}')
else:
    FT = F.transpose()
    Itog = (np.linalg.matrix_power(A,-1) + np.tril(A) - FT) * K #(A^-1 + G - F^T)*K    np.tril(A)-получение нижней треугольной матрицы
    print(f'Матрица Итоговая 2 вариант: \n{Itog}')


from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

fig = plt.figure(figsize=plt.figaspect(0.5))


ax = fig.add_subplot(1, 2, 1, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)


ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()

from mpl_toolkits.mplot3d import Axes3D


v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(v[:, 0], v[:, 1], v[:, 2])
plt.show()



