class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.father = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root : Node, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def in_order(self, root : Node):
        if root is None:
            return
        self.in_order(root.left)
        print(root.key)
        self.in_order(root.right)

    def post_order(self, root : Node):
        if root is None:
            return
        self.in_order(root.left)
        self.in_order(root.right)
        print(root.key)

    def pre_order(self, root: Node):
        if root is None:
            return
        print(root.key)
        self.in_order(root.left)
        self.in_order(root.right)

    def delete(self, root : Node, key):
        if root is None:
            return None
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            else:
                node = root.right
                prev = None
                while node is not None:
                    prev = node
                    node = node.left
                root.key = prev.key
                root.right = self.delete(root.right, prev.key)
                
        return root



tree = BST()
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 20)
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 15)
tree.root = tree.insert(tree.root, 1)
tree.root = tree.delete(tree.root, 10)
tree.pre_order(tree.root)

