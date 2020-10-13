# 1) Бинарный поиск:
# 1.1
def binary_search1(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        count += 1
        if guess == item:
            return mid, count
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, count

n1 = 128
my_list1 = []
for i in range(1,n1 + 1):
    my_list1.append(i)
print(my_list1)
# Макс. кол-во проверок достигается макс. значением переменной
print(binary_search1(my_list1, n1))
# Ответ: 8

#1.2
def binary_search2(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        count += 1
        if guess == item:
            return mid, count
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, count

n2 = 128 * 2
my_list2 = []
for i in range(1,n2 + 1):
    my_list2.append(i)

# Макс. кол-во проверок достигается макс. значением переменной
print(binary_search2(my_list2, n2))
# Ответ: 9

# 1.3, 1.4, 1.5, 1.6 - Х

# 2) Сортировка выбором:
# 2.1 = Список
# 2.2 = Список
# 2.3 = Массив
# 2.4 = При добавлении объекта к динамическому массиву каждый объект может
# переместиться в памяти. Придется сдвигать элементы
# 2.5 = Медленнее

# 3) Рекурсия
# 3.1 = Выполняется внутри функции greet функция greet2
#def greet():
#    greet2()

#def greet2():
# 3.2
def infinityRecursion():
    return infinityRecursion()
print(infinityRecursion())
# Срабатывает exception

# 4) Быстрая сортировка
# 4.1.2/4.2
def r_sum(arr):
    if arr:
        return arr[0] + r_sum(arr[1:])
    return 0

print(r_sum([3, 6, 2, 1]))
# 4.3
def r_biggest(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        biggest = r_biggest(arr[1:])
        return biggest if biggest > arr[0] else arr[0]

print(r_biggest([3, 6, 2, 1]))
# 4.4
