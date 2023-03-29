class Node:
    """Creating Node class, holder of value and next node."""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Creating empty linked list, head,tail is None"""

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend_value(self, value):
        """Insert value at the beginning of the list:
        -create new node --> replace tail of first item in list with new node"""
        new_node = Node(value, self.head)
        print("Prepending value", value)

        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append_value(self, value):
        """Insert value at the end of the list:
        -create new node --> replace head of last item in list with new node"""
        new_node = Node(value, None)

        print("Appending value", value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def traverse(self):
        """Print every node value while current node head is not None."""
        current_node = self.head

        print("Traversing list: ")

        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next_node
        print()

    def find_data(self, value):
        """While current node head is not None, compare node.data with the provided lookup value."""
        current_node = self.head

        print("Finding value", value)

        while current_node is not None:
            if current_node.data == value:
                print("Founded:", current_node.data)
                return current_node
            current_node = current_node.next_node
        print("Value not found!", value)
        return None

    def delete_head(self):
        """Deleting first node"""
        print("Deleting first node")
        if self.head is None:
            return None

        if self.head.next_node is not None:
            self.head = self.head.next_node
        else:
            self.head = None
            self.tail = None

    def toArray(self):
        """While current node head is not None, insert node value into array."""
        print("Creating Array")
        items = []
        current_node = self.head

        while current_node is not None:
            items.append(current_node.data)
            current_node = current_node.next_node

        print(items)


create_list = LinkedList()
# Append few values
create_list.append_value(5)
create_list.append_value(6)
create_list.append_value(7)
create_list.append_value(8)
create_list.append_value(9)
# Prepend value
create_list.prepend_value(10)
# Create Array
create_list.toArray()
# Delete value
create_list.delete_head()
# Traverse List --> print values
create_list.traverse()

# Find data
create_list.find_data(6)  # Value in list
create_list.find_data(10)  # Value not in list
