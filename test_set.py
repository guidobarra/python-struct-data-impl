import unittest

from set_impl import SetImpl


class TestSet(unittest.TestCase):

    def testNotDuplicate(self):
        arrSet = SetImpl()

        arrSet.push(0)
        arrSet.push(7)
        arrSet.push(2)
        arrSet.push(4)
        arrSet.push(3)

        arrSet.push(0)
        arrSet.push(7)
        arrSet.push(2)
        arrSet.push(4)
        arrSet.push(3)

        result = [0, 2, 3, 4, 7]

        self.assertEqual(result, arrSet.getAll())

    def testOneElement(self):
        arrSetByRight = SetImpl()
        arrSetByRight.push(0)

        arrSetByRight.push(10)
        resultElementByRight = [0, 10]

        arrSetByLeft = SetImpl()
        arrSetByLeft.push(0)

        arrSetByLeft.push(-10)
        resultElementByLeft = [-10, 0]

        self.assertEqual(resultElementByRight, arrSetByRight.getAll())
        self.assertEqual(resultElementByLeft, arrSetByLeft.getAll())

    def testSorted(self):
        arrPositive = SetImpl()
        arrNegative = SetImpl()
        arrSet = SetImpl()

        resultPositive = [0, 7, 2, 4, 3, 1, 6, 5, 8, 10]
        resultNegative = [0, -7, -2, -4, -3, -1, -6, -5, -8, -10, -20]
        result = [0, 7, -2, 4, -3, -1, 6, -5, 8, -10, 20]

        for element in resultPositive:
            arrPositive.push(element)

        for element in resultNegative:
            arrNegative.push(element)

        for element in result:
            arrSet.push(element)

        resultPositive = sorted(resultPositive)
        resultNegative = sorted(resultNegative)
        result = sorted(result)

        self.assertEqual(resultPositive, arrPositive.getAll())
        self.assertEqual(resultNegative, arrNegative.getAll())
        self.assertEqual(result, arrSet.getAll())
