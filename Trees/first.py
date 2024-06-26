class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)


def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

def height(node):
    if not node:
        return 0
    l_height = height(node.left) 
    r_height = height(node.right) 
    return max(l_height, r_height) + 1


def print_level(root, level):
    if not root:
        return
    if level == 0:
        print(root.value)
    elif level > 0:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)

def breadth_first(root):
    h = height(root)
    for i in range(h):
        print_level(root, i)