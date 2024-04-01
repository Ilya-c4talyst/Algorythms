# class Stack:

#     def __init__(self):
#         self.__items = []

#     def push(self, item):
#         """Добавить элемент в стек."""
#         self.__items.append(item)

#     def pop(self):
#         """Взять элемент из стека."""
#         return self.__items.pop()

#     def peek(self):
#         """Посмотреть последний элемент без изъятия."""
#         return self.__items[-1]

#     def size(self):
#         """Вернуть размер стека."""
#         return len(self.__items)


"""Стек на списке"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        new = Node(data)
        if not self.top:
            self.top = new
            return
        self.top, new.next = new, self.top

    def pop(self):
        if not self.top:
            return -1
        top = self.top
        if top.next:
            self.top = top.next
        else:
            self.top = None
        return top.data
    