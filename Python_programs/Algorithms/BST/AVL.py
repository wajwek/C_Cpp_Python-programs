class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None


    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x


    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))


    def get_balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)


    def left_rotate(self, node):
        B = node.right
        Y = B.left

        B.left = node
        node.right = Y

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))
        
        return B
    
    
    def right_rotate(self, node):
        B = node.left
        Y = B.right

        B.right = node
        node.left = Y

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left), self.get_height(B.right))

        return B
    
    
    def insert(self, current_node, key):
        if not current_node:
            return Node(key)
        elif key < current_node.key:
            current_node.left = self.insert(current_node.left, key)
        else:
            current_node.right = self.insert(current_node.right, key)

        bf = self.get_balance_factor(current_node)

        if bf > 1 and key < current_node.left.key:
            return self.right_rotate(current_node)

        if bf < -1 and key > current_node.right.key:
            return self.left_rotate(current_node)

        if bf > 1 and key > current_node.left.key:
            current_node.left = self.left_rotate(current_node.left)
            return self.right_rotate(current_node)

        if bf < -1 and key < current_node.right.key:
            current_node.right = self.right_rotate(current_node.right)
            return self.left_rotate(current_node)

        return current_node

    def get_min_node(self, node):
        if node is None:
            return None
        else:
            if self.get_height(node) == 1:
                return node
            elif node.left is not None:
                return self.get_min_node(node.left)
            else:
                return self.get_min_node(node.right)

    def delete(self, current_node, key):
        if not current_node:
            return None
        elif key < current_node.key:
            current_node.left = self.delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self.delete(current_node.right, key)
        else:
            if not current_node.left:
                tmp = current_node.right
                return tmp

            elif not current_node.right:
                tmp = current_node.left
                return tmp

            else:
                tmp = self.get_min_node(current_node.right)
                current_node.key = tmp.key
                current_node.right = self.delete(current_node.right, tmp.key)
                current_node.height = 1 + max(self.get_height(current_node.left), self.get_height(current_node.right))

                bf = self.get_balance_factor(current_node)

                if bf > 1 and self.get_balance_factor(current_node.left) >= 0:
                    return self.right_rotate(current_node)

                if bf < -1 and self.get_balance_factor(current_node.right) <= 0:
                    return self.left_rotate(current_node)

                if bf > 1 and self.get_balance_factor(current_node.left) < 0:
                    current_node.right = self.right_rotate(current_node.right)
                    return self.right_rotate(current_node)

                if bf < -1 and self.get_balance_factor(current_node.right) > 0:
                    current_node.right = self.right_rotate(current_node.right)
                    return self.left_rotate(current_node)

                return current_node


    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def print_inorder(self):
        self.inorder(self.root)
        print()

tree = AVL()

# Wstawianie wartości
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 20)
tree.root = tree.insert(tree.root, 30)
tree.root = tree.insert(tree.root, 40)
tree.root = tree.insert(tree.root, 50)
tree.root = tree.insert(tree.root, 25)

print("Drzewo po wstawieniu:")
tree.print_inorder()

# Wyszukiwanie
print("Szukanie 30:", tree.search(30) is not None)
print("Szukanie 100:", tree.search(100) is not None)

# Usuwanie
tree.root = tree.delete(tree.root, 30)
print("Drzewo po usunięciu 30:")
tree.print_inorder()

# Sprawdzenie balansu (np. wysokość korzenia)
print("Wysokość korzenia:", tree.get_height(tree.root))
