class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        self.head = self._insertEndRecursive(self.head, data)

    def _insertEndRecursive(self, current, data):
        if current is None:
            return Node(data)
        current.next = self._insertEndRecursive(current.next, data)
        return current

    def traverse(self):
        self._traverseRecursive(self.head)

    def _traverseRecursive(self, current):
        if current is None:
            return
        print(current.data, end=" ")
        self._traverseRecursive(current.next)

# Example usage:
ll = LinkedList()
ll.insertEnd(6)
ll.insertEnd(8)
ll.insertEnd(10)
ll.insertEnd(12)
ll.insertEnd(14)
ll.traverse()  # Output: 6 8 10 12 14
