class SetImpl(object):

    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, item):
        if self.length == 0:
            self.arr.append(item)
        else:
            index = self.__getIndexInsert(item)
            if index == -1:
                return
            self.arr.insert(index, item)
        self.length += 1

    def __getIndexInsert(self, item):

        izq = self.length - 1
        der = 0
        middle = 0
        while der <= izq:
            middle = int((izq + der) / 2)
            if self.arr[middle] < item:
                der = middle + 1
            elif self.arr[middle] > item:
                izq = middle - 1
            else:
                break

        if self.arr[middle] < item:
            index = middle + 1
        elif self.arr[middle] > item:
            index = middle
        else:
            index = -1

        return index

    def popFirst(self):
        if self.length == 0:
            return
        item = self.arr.pop(0)
        self.length -= 1
        return item

    def viewFirst(self):
        if self.length == 0:
            return
        return self.arr[0]

    def empty(self):
        return self.length == 0

    def getAll(self):
        return self.arr
