class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Example usage
llist = LinkedList()
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

print("Linked list after inserting 1 at the end:")
llist.print_list()
