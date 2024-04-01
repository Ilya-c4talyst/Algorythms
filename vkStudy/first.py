# def solution(nums, target):
#     newList = []
#     ctZero = 0
#     for i in nums:
#         if i:
#             newList.append(i)
#         else:
#             ctZero += 1
#     return newList + [0 for x in range(ctZero)]
    


# if __name__ == "__main__":
#     size = int(input())
#     nums = [int(x) for x in input().split()]
#     print(*solution(nums, size))


# import inspect


# def print_call_stack():
#     """Функция распечатки имён функций в стеке."""
#     print([frame.function for frame in inspect.stack()])


# class Matryoshka:

#     def __init__(self, size, item=None):
#         self.size = size
#         self.inner_item = item


# def disassemble_matryoshka(matryoshka):
#     """Функция разборки матрёшки."""
#     # Добавим распечатку стека в начале функции.
#     print_call_stack()
#     inner_item = matryoshka.inner_item
#     if inner_item is None:
#         print(f'Все матрёшки разобраны! Размер последней матрёшки: {matryoshka.size}')
#         return
#     # Если внутри что-то есть, то печатаем информационное сообщение...
#     print(f'Разобрали матрёшку размера {matryoshka.size}, разбираем дальше!')
#     disassemble_matryoshka(inner_item)
#     # Добавим распечатку стека в конце функции.
#     print_call_stack()


# if __name__ == '__main__':
#     # Добавим распечатку стека в самом начале выполнения программы.
#     print_call_stack()
#     big_matryoshka = Matryoshka('L', Matryoshka('M', Matryoshka('S')))
#     disassemble_matryoshka(big_matryoshka)
#     # Добавим распечатку стека в конце выполнения программы.
#     print_call_stack()
