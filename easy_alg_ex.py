# Бинарный поиск:
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

# 1.3
