import unittest

from State import State


class MyTestCase(unittest.TestCase):

    def testGetPossibleActionsAllAvailable(self):
        expActions = ["up", "down", "left", "right"]
        self.assertEqual(expActions, State.getActions(State("142608735")))

    def testGetPossibleActionsDownRightOnlyAvailable(self):
        expActions = ["down", "right"]
        self.assertEqual(expActions, State.getActions(State("042618735")))

    def testGetPossibleActionsUpLeftOnlyAvailable(self):
        expActions = ["up", "left"]
        self.assertEqual(expActions, State.getActions(State("142658730")))

    def testGetAllPossibleChildren(self):
        expChildren = ["102648735", "142638705", "142068735", "142680735"]
        children = State.generateChildren(State("142608735"))
        childrenString = []
        for child in children:
            childrenString.append(child.state)
        self.assertEqual(expChildren, childrenString)

    def testGetAllPossibleChildrenDownRightOnlyAvailable(self):
        expChildren = ["642018735", "402618735"]
        children = State.generateChildren(State("042618735"))
        childrenString = []
        for child in children:
            childrenString.append(child.state)
        self.assertEqual(expChildren, childrenString)

    def testGetAllPossibleChildrenUpLeftOnlyAvailable(self):
        expChildren = ["142650738", "142658703"]
        children = State.generateChildren(State("142658730"))
        childrenString = []
        for child in children:
            childrenString.append(child.state)
        self.assertEqual(expChildren, childrenString)


if __name__ == '__main__':
    unittest.main()
