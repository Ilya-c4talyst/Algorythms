class Node:
    """Элемент списка"""
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return self.value


class LinkedList:
    """Связанный список"""
    """Инициализатор"""
    def __init__(self):
        self.head = None


    """Добавление в начало"""
    def add(self, value):
        self.head = Node(value, self.head)


    """Добавление в середину/конец"""  
    def insert(self, index, value):
        if self.head == None or index == 0:
            self.add(value)
        else:
            current = self.head
            while current.next and index > 1:
                current = current.next
                index -= 1
            current.next = Node(value, current.next)


    """Поиск элемента"""
    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    """Поиск длины"""
    def length(self):
        countValues = 0
        current = self.head
        while current:
            countValues += 1
            current = current.next
        return countValues


    """Удаление первого элемента"""
    def remove(self):
        if self.head == None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value


    """Удаление произвольного элемента"""
    def removeAt(self, index):
        if self.head is None or self.head.next is None or index == 0:
            self.remove()
        else:
            current = self.head
            while current.next.next and index > 1:
                current = current.next
                index -= 1
            value = current.next.value
            current.next = current.next.next

            return value
    
    """Представление в виде строки"""
    def __str__(self) -> str:
        toShow = ""
        current = self.head
        while current != None:
            toShow += str(current.value) + "->"
            current = current.next
        return toShow + "None"


link = LinkedList()
link.add(4)
link.add(5)
link.add(6)
link.insert(3, 101)
print(link.contains(101))
print(link.length())
print(link.remove())
print(link)