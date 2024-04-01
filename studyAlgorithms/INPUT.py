# Ввод данных через sys
# name.py

# import sys

# name = sys.stdin.readline().rstrip()  # Применим readline(). и rstrip() для удаления /n
# print(f'Привет, {name}!')

# Правильный ввод и вывод на задаче с получением суммы

# инпут
# 3
# 5 6
# 7 8
# 9 10

# аутпут
# 11
# 15
# 19 

# # Импорт системной библиотеки, 
# # при помощи которой будем считывать данные из стандартного потока ввода.
# import sys


# def main():
#     # Прочитали первую строку, в которой указано количество строк,
#     # преобразовали в число:
#     num_lines = int(sys.stdin.readline().rstrip())  
#     output_numbers = [None] * num_lines
#     # Читаем следующие строки ввода:
#     for i in range(num_lines):
#         # Считали строку и удалили символы перевода строки.
#         line = sys.stdin.readline().rstrip()
#         # Разделили строку по пробельному символу,        
#         # присвоили значения из строки переменным first и second соответственно.
#         first, second = line.split()  
#         # Преобразовали строки в целые числа.
#         first = int(first)  
#         second = int(second)
#         # Получили сумму.
#         result = first + second  
#         # Записали в массив ответов текущий результат как строку.
#         output_numbers[i] = str(result)
#     # В конце вывели все полученные ответы за один раз.
#     print('\n'.join(output_numbers)) 


# if __name__ == '__main__':
#     main()

# распаковка списка
# print(*output_numbers, sep='\n')







# wins = [7495938, 1223125, 2128437, 4567890, 2128500, 2741001, 9314543, 4567687]
# my_ticket = 2128500
# print(enumerate(wins))


wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers)
    while left < right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == element:
            return mid
        if element < sorted_numbers[mid]:
            right = mid
        else:
            left = mid + 1
    return None


# Проверим, что ваш код успешно находит все значения,
# которые есть в списке wins: в качестве искомого элемента
# поочерёдно передадим в функцию все значения из списка.
for item in wins:
    print(find_element(wins, item))