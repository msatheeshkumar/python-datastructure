class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, newnext):
        self.next = newnext

    @next.deleter
    def next(self):
        del self.next

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, newdata):
        self.data = newdata

    @data.deleter
    def data(self):
        del self.data
