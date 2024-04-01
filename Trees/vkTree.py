class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None



"""Высота"""
def height(node):
    if not node:
        return 0
    l_height = height(node.left) 
    r_height = height(node.right) 
    return max(l_height, r_height) + 1

"""Поиск минимума и максимума"""
def minSearh(node):
    if node.left is None:
        return node
    return minSearh(node.left)

def maxSearh(node):
    if node.right is None:
        return node
    return maxSearh(node.right)


"""Поиск в дереве"""
def search(node, val):
    if node is None:
        return None
    if val == node.value:
        return node
    if val < node.value:
        return search(node.left)
    if val > node.value:
        return search(node.right)


"""Обход в ширину"""
def breadth_tree(node):
    root = [node]
    result = []
    while root:
        queue = []
        for current in root:
            result.append(current.val)
            if current.left:
                queue += [current.left]
            if current.right:
                queue += [current.right]
        root = queue
    return result

"""Обход в глубину"""
"""NLR"""
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


"""LRN"""
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


"""LNR"""
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
