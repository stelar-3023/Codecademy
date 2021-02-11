class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# my_node = Node(44)
# print(my_node)
# print(my_node.get_value())

# Create LinkedList class:
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Add your insert_beginning and stringify_list methods below:
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        # link new_node to existing head_node
        new_node.set_next_node(self.head_node)
        # replace current head node with new_node
        self.head_node = new_node

    def stringify_list(self):
        # create empty string to hold values
        string_list = ""
        # track current node starting with the head node
        current_node = self.get_head_node()
        # while we're not at the end of the linked list
        while current_node:
            # get value of the current node
            # convert that to a string
            # add it to the string variable created in the beginning (with a new line)
            if current_node.get_value != None:
                string_list += str(current_node.get_value()) + "\n"
            # move to the next node
            current_node = current_node.get_next_node()
            # once we reach the end of the linked list, return the full string
        return string_list


ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())


# Define remove method below:
def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
    else:
        while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node


remove_node(ll, 70)
print(ll.stringify_list())
