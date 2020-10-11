# 1) binary_search - алгоритм для поиска элемента в отсортированном списке

# Функция бинарного поиска
def binary_search(list, item):
    # Граница начала
    low = 0
    # Граница конца. (-1) так как длина списка с [1 ; n]
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 4, 6, 10, 16, 20, 26]
print(binary_search(my_list, 10))
print(binary_search(my_list, 0))

# 2) Сортировка выбором

# Наименьший элемент массива
def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Используя вышеописанную функцию, пишем сортировку выбором
def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        # Поп меньшего элемента и добавление его к новому массиву
        newArr.append(arr.pop(smallest))
    return newArr

print(SelectionSort([5, 3, 6, 2, 10]))

# 3) Рекурсия

# Через цикл while "поиск ключа в коробках"
def look_for_key_w(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        if item in box:
            pile.append(item)
        elif item.is_a_key():
            print("Found a key!")

# Через рекурсию "поиск ключа в коробках"
def look_for_key_r(box):
    for item in box:
        if item.is_a_box():
            look_for_key_r(item)
        elif item.is_a_key():
            print("Found a key!")

# Ошибка, бесконечная рекурсия
def countdown_error(i):
    print(i)
    countdown_error(i-1)

# Правильная рекурсия
def countdown_correct(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown_correct(i-1)
countdown_correct(10)

# Пример стека
def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name):
    print("How are you, " + name + "?")
def bye():
    print("OK. Bye!")

greet("Mark")

# Вычисление факториала через рекурсию
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x -1)

print(fact(5))
