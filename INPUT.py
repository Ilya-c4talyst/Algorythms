# Ввести одно число
n = int(input())

# Ввести строку

st = input()

# Ввести последовательность << 0 2 3 4 5 6 >>

houses = [int(x) for x in input().split()]
ids = list(map(int, input().split()))

# Собрать несколько последовательностей сразу в список  # << 0 2 3 >>
                                                        # << 6 7 8 >>  [0, 2, 3, 6, 7, 8]
fields = ''.join(input() for _ in range(4))

# Обозначить сразу ряд переменных (через пробел)

a, x, b, c = map(int, input().split())

# Для заполнения матриц

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Пустой список спсков

transp = [[] for _ in range(4)]


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