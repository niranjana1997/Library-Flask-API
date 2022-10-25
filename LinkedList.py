class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def convert_ll_to_list(self):
        lis = []
        if self.head is None:
            return lis

        node = self.head
        while node:
            lis.append(node.data)
            node = node.next
        return lis

    def display_ll(self):
        out = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            out += f" {str(node.data)} ->"
            node = node.next

        out += " None"
        print(out)

    def beginning_insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def end_insert(self, data):
        if self.head is None:
            self.beginning_insert(data)
            return

        self.tail.next = Node(data, None)
        self.tail = self.tail.next

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next
        return None