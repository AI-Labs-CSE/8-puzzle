import unittest

from State import State


class MyTestCase(unittest.TestCase):

    def testGetPossibleActionsAllAvailable(self):
        expActions = ["up", "down", "left", "right"]
        state = State(142608735)
        self.assertEqual(expActions, state.getActions())

    def testGetPossibleActionsDownRightOnlyAvailable(self):
        expActions = ["down", "right"]
        state = State(42618735)
        self.assertEqual(expActions, state.getActions())

    def testGetPossibleActionsUpLeftOnlyAvailable(self):
        expActions = ["up", "left"]
        state =State(142658730)
        self.assertEqual(expActions, state.getActions())

    def testGetAllPossibleChildren(self):
        expChildren = [102648735, 142638705, 142068735, 142680735]
        state = State(142608735)
        children = state.generateChildren()
        childrenString = []
        for child in children:
            childrenString.append(child.stateSavedAsInt)
        self.assertEqual(expChildren, childrenString)

    def testGetAllPossibleChildrenDownRightOnlyAvailable(self):
        expChildren = [642018735, 402618735]
        state = State(42618735)
        children = state.generateChildren()
        childrenString = []
        for child in children:
            childrenString.append(child.stateSavedAsInt)
        self.assertEqual(expChildren, childrenString)

    def testGetAllPossibleChildrenUpLeftOnlyAvailable(self):
        expChildren = [142650738, 142658703]
        state = State(142658730)
        children = state.generateChildren()
        childrenString = []
        for child in children:
            childrenString.append(child.stateSavedAsInt)
        self.assertEqual(expChildren, childrenString)


if __name__ == '__main__':
    unittest.main()
