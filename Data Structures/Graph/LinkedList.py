from Node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        new_node = Node(data)

        if (self.is_empty()):
            self.head = new_node
            return self.head

        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return

    def length(self):
        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def print_linked_list(self):
        if self.is_empty():
            print("List is empty")
            return False

        temp = self.head
        while temp.next is not None:
            print(temp.value, end="->")
            temp = temp.next
        
        print(temp.value, "-> None")
        return True

# ll = LinkedList()
# ll.insert_at_head(5)
# ll.insert_at_head(6)
# ll.insert_at_head(7)
# ll.insert_at_tail(10)

# print(ll.print_linked_list())

