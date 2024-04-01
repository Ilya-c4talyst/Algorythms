class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0 
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value

q = LimitedQueue(8)
# Наполняем с избытком:
for i in range(10):
    q.push(i + 1)
# Напечатаем:
print('В очередь с ограничением 8 добавили 10 элементов:', q.queue)
# Извлекаем:
value = q.pop()
# Печатаем:
print('Извлечено значение', value)
print('Очередь после извлечения одного элемента:', q.queue)
print('Размер очереди после извлечения одного элемента:', q.size)