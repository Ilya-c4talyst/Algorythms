class Queue:
    
    def __init__(self) -> None:
        self.__items = []

    def push(self, value):
        self.__items.insert(0, value)

    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[-1]
    
    def size(self):
        return len(self.__items)