class Nodee:
    def __init__(self, data, next_value):
        self.data = data
        self.next_value = next_value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_value(self, value):
        new_node = Nodee(value, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_value = new_node
            self.tail = new_node

    def toArray(self):
        items = []
        current_node = self.head

        while current_node is not None:
            items.append(current_node.data)
            current_node = current_node.next_value

        print(items)


create_list = LinkedList()
create_list.append_value(5)
create_list.append_value(6)
create_list.append_value(7)
create_list.toArray()
