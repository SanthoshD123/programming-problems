class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def count_and_sum(self):
        count = 0
        total_sum = 0
        current_node = self.head
        while current_node:
            count += 1
            total_sum += current_node.data
            current_node = current_node.next
        return count, total_sum

# Example usage:
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

count, total_sum = linked_list.count_and_sum()
print("Count:", count)
print("Sum:", total_sum)
