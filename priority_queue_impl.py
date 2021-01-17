from set_impl import SetImpl


class PriorityQueueImpl(object):

    def __init__(self):
        self.queue = {}
        self.priority = SetImpl()
        self.length = 0

    def push(self, item, priority):
        if self.queue.get(priority) is None:
            self.queue[priority] = []
        self.queue[priority].append(item)
        self.priority.push(priority)

    def pop(self):
        item = None

        while item is None and not self.priority.empty():
            p = self.priority.viewFirst()
            tam = len(self.queue.get(p))
            if tam > 1:
                item = self.queue.get(p).pop(0)
            elif tam == 1:
                self.priority.popFirst()
                item = self.queue.get(p).pop(0)
            else:
                self.priority.popFirst()
        return item

    def empty(self):
        return self.priority.empty()

    def getAll(self):
        result = []
        for key in self.priority.getAll():
            if self.queue.get(key) is None:
                continue
            else:
                result.append(self.queue[key])
        return result
