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

# with open('input.txt', 'r', encoding='utf-8') as file:
#     read_file = file.read()
#     lines = read_file.split('\n')
#     cases = int(lines[0])
#     result = []
#     for i in range(2, len(lines), 2):
#         massive = [int(elem) for elem in lines[i].split()]
#         test = []
#         result = []
#         i=0
#         while i < len(massive):
#             if not test:
#                 test.append(massive[i])
#                 i+=1
#                 continue
#             if massive[i] < len(test) + 1 or len(test) + 1 > min(test):
#                 result.append(len(test))
#                 test.clear()
#                 test.append(massive[i])
#             else:
#                 test.append(massive[i])
#             i+=1
#         if test:
#             if len(test) > min(test):
#                 diff = len(test) - min(test)
#                 result[-1] -= diff
#                 result.append(len(test)+diff)
#             else:
#                 result.append(len(test))
#         with open('output.txt', 'a') as file:
#             file.write(str(len(result)) + '\n')
#             for j in result:
#                 file.write(str(j) + ' ')
#             file.write('\n')
with open('input.txt', 'r', encoding='utf-8') as file:
    read_file = file.read()
    lines = read_file.split('\n')
    cases = int(lines[0])
    result = []
    for i in range(1, cases * 2 + 1, 2):
        h = int(lines[i])
        massive = [int(elem) for elem in lines[i+1].split()]
        with open('output.txt', 'a') as file:
            file.write(str(len(result)) + '\n')
            for j in result:
                file.write(str(j) + ' ')
            file.write('\n')