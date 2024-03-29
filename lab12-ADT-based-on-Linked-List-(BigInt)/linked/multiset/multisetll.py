from node import *
       

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """Removes all element and return list"""
        data = []
        while self._head != None:
            data.append(self._head.item)
            self.delete(data[-1])
        return data

    def split_half(self):
        """Splites multiset to two multisets"""
        if self._head == None or self._head.next == None:
            return None
        length = 0
        prob = self._head
        while prob != None:
            prob = prob.next
            length += 1
        half = int(length/2)
        first, second = Multiset(), Multiset()
        print(length, half)
        
        prob = self._head
        i = 0
        while i != half:
            i += 1
            previous = prob
            prob = prob.next
        second._head = prob
        first._head = self._head
        previous.next = None

        return first, second
