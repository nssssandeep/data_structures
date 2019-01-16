class SingleLinkedList(object):
    '''This is Single Linked List ADT implementation. This supports the below methods'''

    def __init__(self, head=None):
        self.head = head

    def insert_from_list(self, list_values):
        pass

    def add(self, data, position):
        pass

    def remove(self, position):
        pass


class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
