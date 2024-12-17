'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. 
Обязательное требование – минимизация времени выполнения и объема памяти.
18.	F(0) = 1, F(1) = 1, F(n) = (-1)n*(F(n–1) /(2n)!*F(n-2)+1), при n > 1'''

import timeit
perem, fact1, minus = 1, 2, 1
while perem ==1:
    n = int(input('Введите n: '))
    if n>1:
        def factre(n): 
            if n == 1 or n == 0:
                factr = 1
            else:
                factr = n * factre(n-1)
            return factr   
        def Fr(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            else:
                if n%2==0:
                    return 1 * (((Fr(n-1)/factre(2*n)) *Fr(n-2)) +1)
                else:
                    return (-1) * (((Fr(n-1)/factre(2*n)) *Fr(n-2)) +1)
   
        a =timeit.timeit('Fr(n)', globals = globals(), number =1)
        print(f'Рекурсивно.Функция: {Fr(n)} \nВремя: {a}')
        
    
        def Fi(n, fact1, minus):
            second, first = 1,1
            for i in range(0,n+1):
                if i == 0:
                    answer = 1
                elif i == 1:
                    answer = 1
                else:
                    fact1 = fact1 * (i*2) * ((i*2)-1)
                    answer = minus *(((first/fact1) *second)+1)
                    #answer = 1 * (one/fact1 - 2*two /fact2)
                    second, first = first, answer
                    minus*=-1 
                          
            return answer

        a =timeit.timeit('Fi(n, fact1, minus)', globals = globals(), number =1)
        print(f'Функция: {Fi(n, fact1,minus)} \nВремя: {a}')
        perem =2
    else:print('Число должно быть больше 1')




