# Бинарный поиск:
# 1.1
def binary_search(list, item):
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

n = 128
my_list = []
for i in range(1,n+1):
    my_list.append(i)
print(my_list)
# Макс. кол-во проверок достигается макс. значением переменной
print(binary_search(my_list, n))
# Ответ: 8

#1.2
def binary_search(list, item):
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

n = 128 * 2
my_list = []
for i in range(1,n+1):
    my_list.append(i)
print(my_list)
# Макс. кол-во проверок достигается макс. значением переменной
print(binary_search(my_list, n))
# Ответ: 9

# 1.3
