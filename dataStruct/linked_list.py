class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


# class Box:
#   def __init__ (self,cat = None):
#     self.cat = cat
#     self.nextcat = None

# class LinkedList:
#   def __init__(self):
#     self.head = None

# my_list = LinkedList()
# box1 = Box("Cat 1")
# my_list.head = box1
# box2 = Box("Cat 2")
# box1.nextcat = box2
# box3 = Box("Cat 3")
# box2.nextcat = box3

# current = my_list.head
# while current is not None:
#     print(current.cat)
#     current = current.nextcat