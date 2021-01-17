import unittest

from priority_queue_impl import PriorityQueueImpl


class TestPriorityQueue(unittest.TestCase):

    def testOneElement(self):
        pqLeft = PriorityQueueImpl()
        pqLeft.push("level meddle", 1)
        pqLeft.push("level low", 2)

        pqRight = PriorityQueueImpl()
        pqRight.push("level meddle", 1)
        pqRight.push("level critical", 0)

        pq = PriorityQueueImpl()
        pq.push("level meddle", 1)
        pq.push("level critical", 0)
        pq.push("level low", 2)

        resultLeft = [["level meddle"], ["level low"]]
        resultRight = [["level critical"], ["level meddle"]]
        result = [["level critical"], ["level meddle"], ["level low"]]

        self.assertEqual(resultLeft, pqLeft.getAll())
        self.assertEqual(resultRight, pqRight.getAll())
        self.assertEqual(result, pq.getAll())

        total = [(resultLeft, pqLeft), (resultRight, pqRight), (result, pq)]

        for (r, p) in total:
            for ar in r:
                for element in ar:
                    self.assertEqual(element, p.pop())

    def testSelfPriority(self):
        pq = PriorityQueueImpl()

        pq.push("level 2, passer one", 2)
        pq.push("level 2, passer two", 2)
        pq.push("level 2, passer three", 2)
        pq.push("level 2, passer four", 2)
        pq.push("level 2, passer five", 2)
        pq.push("level 2, passer six", 2)

        result = [["level 2, passer one", "level 2, passer two", "level 2, passer three",
                   "level 2, passer four", "level 2, passer five", "level 2, passer six"]]

        self.assertEqual(result, pq.getAll())

        for ar in result:
            for element in ar:
                self.assertEqual(element, pq.pop())

    def testPriorityAscendant(self):
        pq = PriorityQueueImpl()

        pq.push("level 0, passer one", 0)
        pq.push("level 2, passer one", 2)
        pq.push("level 2, passer two", 2)
        pq.push("level 3, passer one", 3)
        pq.push("level 3, passer two", 3)
        pq.push("level 3, passer three", 3)

        result = [["level 0, passer one"],
                  ["level 2, passer one", "level 2, passer two"],
                  ["level 3, passer one", "level 3, passer two", "level 3, passer three"]]

        self.assertEqual(result, pq.getAll())

        for ar in result:
            for element in ar:
                self.assertEqual(element, pq.pop())

    def testPriorityFalling(self):
        pq = PriorityQueueImpl()

        pq.push("level 3, passer one", 3)
        pq.push("level 3, passer two", 3)
        pq.push("level 3, passer three", 3)
        pq.push("level 2, passer one", 2)
        pq.push("level 2, passer two", 2)
        pq.push("level 0, passer one", 0)

        result = [["level 0, passer one"],
                  ["level 2, passer one", "level 2, passer two"],
                  ["level 3, passer one", "level 3, passer two", "level 3, passer three"]]

        self.assertEqual(result, pq.getAll())

        for ar in result:
            for element in ar:
                self.assertEqual(element, pq.pop())

    def testPriorityRandom(self):
        pq = PriorityQueueImpl()

        pq.push("level 3, passer one", 3)
        pq.push("level 0, passer one", 0)
        pq.push("level 3, passer two", 3)
        pq.push("level 2, passer one", 2)
        pq.push("level 3, passer three", 3)
        pq.push("level 2, passer two", 2)

        result = [["level 0, passer one"],
                  ["level 2, passer one", "level 2, passer two"],
                  ["level 3, passer one", "level 3, passer two", "level 3, passer three"]]

        self.assertEqual(result, pq.getAll())
        for ar in result:
            for element in ar:
                self.assertEqual(element, pq.pop())

    def testEmpty(self):
        pq = PriorityQueueImpl()

        self.assertEqual(True, pq.empty())

    def testEmptyWithElement(self):
        pq = PriorityQueueImpl()

        pq.push("level 3, passer one", 3)
        pq.push("level 0, passer one", 0)
        pq.push("level 3, passer two", 3)

        self.assertEqual(False, pq.empty())
        pq.pop()
        self.assertEqual(False, pq.empty())
        pq.pop()
        self.assertEqual(False, pq.empty())
        pq.pop()
        self.assertEqual(True, pq.empty())

    def testEmptyQueuePop(self):
        pq = PriorityQueueImpl()

        self.assertEqual(None, pq.pop())
