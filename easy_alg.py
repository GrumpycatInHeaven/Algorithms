#1) binary_search - алгоритм для поиска элемента в отсортированном списке
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
