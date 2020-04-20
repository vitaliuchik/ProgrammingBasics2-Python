class Carousel:
    """Represents carousel"""

    def __init__(self, tipe, capacity):
        """Initializes type, capacity of carousel"""
        self._type = tipe
        self._capacity = capacity
        self._children = []

    def __str__(self):
        """Represetns carousel in string"""
        return "{} house {}: {}".format(self._type, self._capacity,\
                                        self._children)

    def add_child(self, child):
        """Adds child to carousel
        :param child: str
        :returns bool"""
        if len(self._children) == self._capacity:
            return False
        self._children.append(child)
        return True

    def remove_child(self, mom_call=None):
        """Remove child from carousel
        :param child: str
        :returns bool or called child"""
        if mom_call is None and len(self._children) > 0:
            self._children.pop()
            return True
        if mom_call in self._children and len(self._children) > 0:
            self._children.remove(mom_call)
            return mom_call
        return False

    def __eq__(self, other):
        """Checks if equal by tipe and capacity"""
        if not isinstance(other, self.__class__):
            return False
        return self._type == other._type and self._capacity == other._capacity

    def __ne__(self, other):
        """Checks if not equal by tipe and capacity"""
        if not isinstance(other, self.__class__):
            return True
        return self._type != other._type or self._capacity != other._capacity


class Attraction(Carousel):
    """Represents attraction (carousel's child)"""

    def __init__(self, tipe, capacity, supervisor):
        """Initializes type, capacity and supervisor of carousel"""
        super().__init__(tipe, capacity)
        self.add_child(supervisor)
        self._started = False

    def start_attraction(self):
        """Starts attraction"""
        self._started = True

    def stop_attraction(self):
        """Stops attraction"""
        self._started = False

    def remove_child(self, mom_call=None):
        """Removes child from carousel (doesn't remove supervisor)
        param child: str
        :returns bool or called child"""
        if not self._started:
            if mom_call is None and len(self._children) > 1:
                self._children.pop()
                return True
            if mom_call in self._children and len(self._children) > 1:
                self._children.remove(mom_call)
                return mom_call
        return False