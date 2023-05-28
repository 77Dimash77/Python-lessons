# Задача 1. Дан список элементов. Используя библиотеку NumPy,
# подсчитайте количество уникальных элементов в нём.
def Zadacha1():
  import numpy as np
  elements = [1, 2, 3, 4, 1, 2, 3, 4, 5]
  arr = np.array(elements)
  unique_count = len(np.unique(arr))
  print("Количество уникальных элементов:", unique_count)


# Задача 2. Создайте двумерный массив, размером 5х5. Определите, 
# есть ли в нём одинаковые строки.
def Zadacha2():
  import numpy as np
  arr = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [1, 2, 3, 4, 5],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])
  unique_rows = np.unique(arr, axis=0)
  has_duplicate_rows = len(unique_rows) != len(arr)
  if has_duplicate_rows:
      print("В массиве есть одинаковые строки")
  else:
      print("В массиве нет одинаковых строк")


# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.
def Zadacha3():
  import numpy as np
  rows = np.random.randint(2, 6) 
  cols = np.random.randint(2, 6) 
  arr = np.random.randint(1, 10, size=(rows, cols))
  max_index = np.unravel_index(np.argmax(arr), arr.shape)
  min_index = np.unravel_index(np.argmin(arr), arr.shape)
  print("Индекс максимального элемента:", max_index)
  print("Индекс минимального элемента:", min_index)
  diagonal = np.diagonal(arr)
  print("Элементы главной диагонали:", diagonal)
