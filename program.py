N = int(input())  # ввод количества чисел
a = [int(input()) for i in range(N)]  # ввод элементов массива, то есть заданных чисел в столбик
for i in range(N):
    summa = 0  # обнуление суммы цифр числа
    while a[i] > 0:  # это начало цикла
        summa = summa + a[i] % 10  # последняя цыфра в числе
        a[i] = a[i] // 10  # отбрасывание последней цифры в числе
        if summa <= 9:  # условие проверки суммы цифр
            print(summa)
        else:  # если сумма цифр больше 9, то продолжаем складывать цифры
            a[i] = summa
            summa = 0
            while a[i] > 0:
                summa = summa + a[i] % 10
                a[i] = a[i] // 10
                print(summa)
