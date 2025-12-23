
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right

    def contains(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def empty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def min(self):
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def max(self):
        if self.root is None:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def sorted(self):
        result = []
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.value)
            node = node.right
        return result

    def in_range(self, min_value, max_value):
        result = []
        stack = [self.root] if self.root else []
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.value >= min_value:
                stack.append(node.left)
            if min_value <= node.value <= max_value:
                result.append(node.value)
            if node.value <= max_value:
                stack.append(node.right)
        result.sort()
        return result

    def remove(self, value):
        if self.root is None:
            return
        if self.root.value == value:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                node = self.root.right
                while node.left:
                    node = node.left
                self.root.value = node.value
                self.root.right = self.remove_node(self.root.right, node.value)
            return
        
        parent = self.root
        node = self.root
        is_left = False
        
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
                is_left = True
            else:
                node = node.right
                is_left = False
        
        if node is None:
            return
        
        if node.left is None and node.right is None:
            if is_left:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None:
            if is_left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if is_left:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.value = successor.value
            if successor_parent == node:
                node.right = successor.right
            else:
                successor_parent.left = successor.right

    def remove_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.remove_node(node.left, value)
        elif value > node.value:
            node.right = self.remove_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = self.remove_node(node.right, successor.value)
        return node

    def display(self):
        def show(node, prefix="", is_left=True):
            if node.right:
                show(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            if node.left:
                show(node.left, prefix + ("    " if is_left else "│   "), True)
        if self.root:
            show(self.root)


if __name__ == "__main__":
    tree = BinaryTree()
    for i in [7, 2, 9, 1, 5, 8, 10, 3]:
        tree.insert(i)

    tree.display()
    print(tree.contains(5))
    print(tree.contains(11))