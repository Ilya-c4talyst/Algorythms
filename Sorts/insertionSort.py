nums = [1,4,2,3,5,8,7,9]

def insertionSort(nums):
    
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and current < nums[j]:
            nums[j+1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums

# n = int(input())
# nums = [int(x) for x in input().split()]
print(*insertionSort(nums))
            
        


# # Длины слов "ноль", "один", "два", "три", "четыре" - и так до двенадцати.
# digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]


# def card_strength(idx):
#     # Получаем количество букв для числа idx.
#     return digit_lengths[idx]


# # Добавляем в функцию параметр key,
# # в него будет передана функция, получающая значение ключа сортировки.
# def insertion_sort_by_key(arr, key):
#     for i in range(1, len(arr)):
#         current = arr[i]
#         prev = i - 1
#         # При сравнении элементов вызываем функцию, переданную в параметр key, 
#         # она вернёт значение ключа.
#         while prev >= 0 and key(arr[prev]) > key(current):
#             arr[prev + 1] = arr[prev]
#             prev -= 1
#         arr[prev + 1] = current


# cards = [2, 9, 11, 7, 1]
# # При вызове сортировки передаём в параметры функцию,
# # возвращающую значение ключа.
# insertion_sort_by_key(cards, card_strength)
# # Для контроля - напечатаем результат:
# print(cards)
        


# digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]


# def card_strength(idx):
#     return digit_lengths[idx]


# cards = [2, 9, 11, 7, 1]
# # В параметр key передаём функцию, возвращающую значения ключей.
# result = sorted(cards, key=card_strength)
# print(result)