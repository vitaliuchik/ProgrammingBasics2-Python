from node import Node


class Struct:
    def __init__(self):
        self._head = None

    def add(self, value):
        if self._head is None:
            self._head = Node(value)
        else:
            next_el = self._head
            self._head = Node(value)
            self._head.next = next_el





def search(head):
    average = head
    all_len = head
    while average != None:
        average = average.next
        try:
            all_len = all_len.next.next
        except AttributeError:
            break
    return exp.data


