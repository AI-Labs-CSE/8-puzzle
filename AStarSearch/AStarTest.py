import unittest

from AStar import AStar
from State.State import State


class MyTestCase(unittest.TestCase):
    def testEasyPuzzleManhattan(self):
        astar = AStar(State(125340678), State(12345678), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0], ["up", "left", "left"])

    def testEasyPuzzleEuclidian(self):
        astar = AStar(State(125340678), State(12345678), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0], ["up", "left", "left"])

    def testSolvePuzzleWithDepth27Manhattan(self):
        astar = AStar(State(54861732), State(12345678), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[1], 26)

    def testSolvePuzzleWithDepth27Euclidian(self):
        astar = AStar(State(54861732), State(12345678), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[1], 26)

    def testCompareExpandOfPuzzleWithDepth27ManhattanAndEuclidian(self):
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
        self.assertEqual(report[1],31)

    def testComplexProblemEuclidian(self):
        initialState = State(867254301)
        goalState = State(123456780)
        astar = AStar(initialState, goalState, "euclidian")
        report = astar.getReport()
        self.assertEqual(report[1], 31)

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
