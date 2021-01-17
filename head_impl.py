class HeapImpl(object):

    def __init__(self, priority="Min"):
        self.arr = []
        self._priority = priority
        self.length = 0

    def push(self, item):
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.arr.pop(0)

    def empty(self):
        return self.length == 0



