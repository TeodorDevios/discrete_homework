class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, value):
        if index == 0:
            self.append_first(value)
            return
        current = self.head
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if not current:
            return
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def get(self, index):
        current = self.head
        for i in range(index):
            if not current:
                return None
            current = current.next
        if not current:
            return None
        return current.value

    def remove(self, index):
        if index == 0:
            self.remove_first()
            return
        current = self.head
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if not current or not current.next:
            return
        current.next = current.next.next

    def remove_first(self):
        if self.head:
            self.head = self.head.next

    def remove_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def clear(self):
        self.head = None

    def print_all(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

if __name__ == "__main__":
    lst = LinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    lst.print_all()