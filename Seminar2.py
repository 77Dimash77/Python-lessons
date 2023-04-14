# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def Zadacha1(n):
    r = []
    for i in range(1, n + 1):
        f = 1
        for j in range(1, i + 1):
            f *= j
        r.append(f)
    return r
    n = int(input("Введите число N: "))
    fs = Zadacha1(n)
    print(fs)


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def Zadacha2():
    print("X  |  Y  |  Z  |  ¬(X ∧ Y) ∨ Z")
    print("-------------------------------")
    for X in [0, 1]:
        for Y in [0, 1]:
            for Z in [0, 1]:
                result = not (X and Y) or Z
                print(f"{X}  |  {Y}  |  {Z}  |       {int(result)}")

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def Zadacha3():
    x = input("Введите первую строку: ")
    y = input("Введите вторую строку: ")
    for i in x:
        count = 0
        for j in y:
            if i == j:
                count += 1
        print(i, "-", count)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def zadacha4():
    N = int(input('Введите число: '))
    numbers = list(range(-N, N + 1))
    print("Исходный список:", numbers)
    shifted_numbers = numbers[-2:] + numbers[:-2]
    print("Сдвинутый список:", shifted_numbers)
