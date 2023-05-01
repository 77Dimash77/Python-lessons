# Урок 6. Повторение списков

# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396
def Zadacha1():
    N = str(input('Введите чило N: '))
    Chislo1 = N
    Chislo2 = N + N
    Chislo3 = N + N + N
    print(Chislo1,Chislo2,Chislo3)
    print(int(Chislo1) + int(Chislo2) + int(Chislo3))

# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
def Zadacha2():
    import random
    chislo = str(input('Введите число: '))
    sluch_spisok = [random.randint(0,1) for _ in range(15)]
    print(sluch_spisok)
    sluch_spisok_str = ''.join(map(str, sluch_spisok))
    trio = ''
    count = 0
    win = 0
    for i in sluch_spisok_str:
        if count < 3:
            trio += i
            count += 1
            if count == 3:
                if trio == chislo:
                  print('Число есть в массиве')
                  win += 1
        else:
            trio = trio[1:] + i
            if count < 15:
                count += 1
                if trio == chislo:
                    print('Число есть в массиве')
                    win += 1
            else:
                break
    if win < 1:
        print('Такого числа нет')

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
def Zadacha3():
  def nod(a, b):
      while b:
          a, b = b, a % b
      return a
  def nayti_drobi(max_znamenatel):
      drobi = []
      for znamenatel in range(1, max_znamenatel + 1):
          for chislitel in range(1, znamenatel):
              if nod(chislitel, znamenatel) == 1:
                  drobi.append((chislitel, znamenatel))
      return drobi
  max_znamenatel = 11
  drobi = nayti_drobi(max_znamenatel)
  print("Prostye nesokratimye drobi:")
  for drob in drobi:
      print(f"{drob[0]}/{drob[1]}")