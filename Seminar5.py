# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
#  Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
def Zadacha1():
  import random
  num = [random.randint(1,10) for _ in range(10)]
  print(num)
  x = filter(lambda x: x>5, num)
  x = list(x)
  print(x)


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.\

def Zadacha2():
  import random
  sluchSpisok = [random.randint(1,10) for _ in range(10)]
  print(f'{sluchSpisok} список случайных чисел')
  itogSpisok = []
  startcifra = random.choice(sluchSpisok)
  SpisokSoglCifr = []
  print(f'{startcifra} цифра с которой идет отчет')
  max = 0
  for i in sluchSpisok:
    if i > max:
      max = i
  print(f'{max} максимальное число')
  for i in sluchSpisok:
    if i > startcifra:
      SpisokSoglCifr.append(i)
  SpisokSoglCifr = list(set(SpisokSoglCifr))
  SpisokSoglCifr.sort()
  print(f'{SpisokSoglCifr} список цифр которые поподают в диапозон')
  diapozonMax = len(SpisokSoglCifr)
  print(f'{diapozonMax} максимальный диапазон')
  diapozonLength = random.randint(1,diapozonMax)
  print(f'{diapozonLength} длинна порядка')
  itogSpisok = [startcifra, ]
  count = 0
  for i in SpisokSoglCifr:
    if count < diapozonLength - 1:
      itogSpisok.append(i)
      count += 1
  print(f'{itogSpisok} итоговый список')

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, 
# сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
def Zadacha3():
  import random
  sluchSpisok = [random.randint(1,10) for _ in range(10)]
  print(sluchSpisok )
  sluchSpisok = list(set(sluchSpisok))
  print(sluchSpisok )
  print(f'{(10 - (len(sluchSpisok)))*2} элиментов(а) совпадает')

# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.
  line1 = [1,2,3]
  line2 = [4,5,6]
  line3 = [7,8,9]
  table = [line1, line2, line3]
  x = input('ход первого игрока: ')
  o = input('ход второго игрока: ')
  hod = 1
  
  if line1 == [x, x, x] or [o, o, o]:
    print('игра завершина')
    if line1 == [x, x, x]:
        print('Победил "x"')
    elif line1 == [o, o, o]:
        print('Победил "o"')
  if line2 == [x, x, x] or [o, o, o]:
    print('игра завершина')
    if line2 == [x, x, x]:
        print('Победил "x"')
    elif line2 == [o, o, o]:
        print('Победил "o"')
  if line3 == [x, x, x] or [o, o, o]:
    print('игра завершина')
    if line3 == [x, x, x]:
        print('Победил "x"')
    elif line3 == [o, o, o]:
        print('Победил "o"')  

  if line1[0] == x or o and line2[0] == x or o and line3[0] == x or o:
    print('игра завершина')
    if line1 == [x, x, x]:
        print('Победил "x"')
    elif line1 == [o, o, o]:
        print('Победил "o"')