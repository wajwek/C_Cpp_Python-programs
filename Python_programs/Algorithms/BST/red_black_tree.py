class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = "red"
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts an element into the Red-Black Tree"""
        if self.root is None:
            self.root = Node(key)
            self.root.color = "black"
            return
        
        # Standard BST insertion
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        # Creating a new node
        new_node = Node(key)
        new_node.parent = parent
        
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # Balancing
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        """Fixes colors after insertion"""
        while node.parent is not None and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)
        self.root.color = "black"

    def _left_rotate(self, node):
        """Left rotation - returns the new root of the subtree"""
        right_child = node.right
        if right_child is None:
            return node
        
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        
        right_child.left = node
        node.parent = right_child
        return right_child

    def _right_rotate(self, node):
        """Right rotation - returns the new root of the subtree"""
        left_child = node.left
        if left_child is None:
            return node
        
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        
        left_child.right = node
        node.parent = left_child
        return left_child

    def delete(self, key):
        """Deletes an element from the tree"""
        node = self._search_node(key)
        if node is None:
            return
        
        self._delete_node(node)

    def _search_node(self, key):
        """Searches for a node with a given key"""
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def _delete_node(self, node):
        """Deletes a node from the tree"""
        # Node has two children
        if node.left is not None and node.right is not None:
            successor = self._find_min(node.right)
            node.key = successor.key
            node = successor
        
        # Node has 0 or 1 child
        child = node.left if node.left is not None else node.right
        
        if node.color == "red":
            # Red node - simple deletion
            if node.parent is None:
                self.root = child
            else:
                if node == node.parent.left:
                    node.parent.left = child
                else:
                    node.parent.right = child
                if child:
                    child.parent = node.parent
        else:
            # Black node - balancing
            if child is not None:
                child.color = "black"
                if node.parent is None:
                    self.root = child
                else:
                    if node == node.parent.left:
                        node.parent.left = child
                    else:
                        node.parent.right = child
                    child.parent = node.parent
            else:
                if node.parent is None:
                    self.root = None
                else:
                    if node == node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None

    def _find_min(self, node):
        """Finds the node with the minimum key"""
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self, node=None, prefix="", is_left=None):
        """Prints the tree in a readable format with colors"""
        if node is None:
            node = self.root
        
        if node is None:
            print("Tree is empty")
            return
        
        color_str = f" [{node.color.upper()}]"
        if is_left is None:  # Root
            print(str(node.key) + color_str)
        else:
            connector = "|-- " if is_left else "`-- "
            print(prefix + connector + str(node.key) + color_str)
        
        if node.left is not None or node.right is not None:
            if node.left is not None:
                extension = "|   " if node.right is not None else "    "
                self.print_tree(node.left, prefix + extension, True)
            if node.right is not None:
                extension = "    "
                self.print_tree(node.right, prefix + extension, False)

    def in_order(self, node=None):
        """Lists elements in in-order"""
        if node is None:
            node = self.root
        if node is None:
            return
        result = []
        self._in_order_helper(node, result)
        print(" ".join(map(str, result)))
    
    def _in_order_helper(self, node, result):
        if node is None:
            return
        self._in_order_helper(node.left, result)
        result.append(node.key)
        self._in_order_helper(node.right, result)


# ===== TESTS =====
print("="*60)
print("TEST 1: Inserting elements into Red-Black Tree")
print("="*60)
tree = RedBlackTree()
elements = [10, 5, 15, 3, 7, 12, 17, 1, 4, 6, 8]

for elem in elements:
    tree.insert(elem)
    print(f"Inserted {elem}")

print("\nTree structure:")
tree.print_tree()

print("\nIn-order:")
tree.in_order()
print()

print("\n" + "="*60)
print("TEST 2: Deleting an element (10)")
print("="*60)
tree.delete(10)
print("Tree structure after deletion:")
tree.print_tree()
print("\nIn-order:")
tree.in_order()
print()

print("\n" + "="*60)
print("TEST 3: Deleting an element (5)")
print("="*60)
tree.delete(5)
print("Tree structure after deletion:")
tree.print_tree()
print("\nIn-order:")
tree.in_order()
print()

print("\n" + "="*60)
print("TEST 4: Deleting an element (1) - leaf")
print("="*60)
tree.delete(1)
print("Tree structure after deletion:")
tree.print_tree()
print("\nIn-order:")
tree.in_order()
print()
