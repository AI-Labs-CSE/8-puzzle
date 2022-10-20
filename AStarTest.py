import unittest

from AStar import AStar
from State import State


class MyTestCase(unittest.TestCase):
    def testEasyPuzzleManhattan(self):
        astar = AStar(State(125340678), State(12345678), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0], ["Up", "Left", "Left"])

    def testEasyPuzzleEuclidian(self):
        astar = AStar(State(125340678), State(12345678), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0], ["Up", "Left", "Left"])

    def testSolvePuzzleWithDepth27Manhattan(self):
        astar = AStar(State(54861732), State(12345678), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['Right', 'Right', 'Down', 'Left', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down', 'Left',
                          'Up', 'Left', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down',
                          'Left', 'Left', 'Up'])

    def testSolvePuzzleWithDepth27Euclidian(self):
        astar = AStar(State(54861732), State(12345678), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['Right', 'Down', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down', 'Left', 'Left', 'Up', 'Up',
                          'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Down', 'Left', 'Up',
                          'Right', 'Up', 'Left'])

    # this state is made to dimostrant that a* is better in case of manhattan than euclidian
    # because in bid test cases manhattan hs less expand nodes than euclidian
    def testcompareExpandOfPuzzleWithDepth27ManhattanAndEuclidian(self):
        astarM = AStar(State(54861732), State(12345678), "manhattan")
        reportM = astarM.getReport()
        astarD = AStar(State(54861732), State(12345678), "euclidian")
        reportD = astarD.getReport()
        self.assertLess(reportM[2], reportD[2])

    def testComplexProblemManhattan(self):
        initialState = State(867254301)
        goalState = State(123456780)
        astar = AStar(initialState, goalState, "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Down', 'Right', 'Right', 'Up', 'Left', 'Left',
                          'Down', 'Right', 'Right', 'Up', 'Left', 'Up', 'Right', 'Down', 'Left', 'Up', 'Left', 'Down',
                          'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Right'])

    def testComplexProblemeEuclidian(self):
        initialState = State(867254301)
        goalState = State(123456780)
        astar = AStar(initialState, goalState, "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['Left', 'Up', 'Right', 'Up', 'Right', 'Down', 'Down', 'Left', 'Up', 'Up', 'Right', 'Down',
                          'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Left', 'Left', 'Down', 'Right',
                          'Up', 'Left', 'Up', 'Right', 'Down', 'Right', 'Down'])

    def testUnsolvableManhattan(self):
        initialState = State(812043765)
        goalState = State(123456780)
        astar = AStar(initialState, goalState, "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0], [])

    def testUnsolvableEuclidian(self):
        initialState = State(812043765)
        goalState = State(12345678)
        astar = AStar(initialState, goalState, "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0], [])


if __name__ == '__main__':
    unittest.main()
