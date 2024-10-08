''' This is a program to learn about nodes and linked lists. '''

class Node:
    '''This is a class for a node in a linked list.'''
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

        # Define set_link_node method below:

    def set_link_node(self, link_node):
        '''Sets the link node'''
        self.link_node = link_node

    def get_link_node(self):
        '''Returns the link node'''
        return self.link_node

    def get_value(self):
        '''Returns the value of the node'''
        return self.value

    # instantiate 3 nodes


yacko = Node('likes to yak')
wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')
# give dot a link_node of wacko
dot.set_link_node(wacko)
# give yacko a link_node of dot
yacko.set_link_node(dot)
# create variable / user getter methods
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)
