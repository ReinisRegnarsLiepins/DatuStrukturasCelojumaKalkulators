class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def pop(self, index):
        if index < 0:
            raise IndexError

        current = self.head

        if index == 0:
            if current:
                self.head = current.next
            return

        prev = None
        for _ in range(index):
            prev = current
            if not current or not current.next:
                raise IndexError
            current = current.next

        prev.next = current.next

