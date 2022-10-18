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
        self.assertEqual(report[0],
                         ['right', 'right', 'down', 'left', 'left', 'down', 'right', 'up', 'right', 'down', 'left',
                          'up', 'left', 'down', 'right', 'up', 'up', 'left', 'down', 'right', 'up', 'right', 'down',
                          'left', 'left', 'up'])

    def testSolvePuzzleWithDepth27Euclidian(self):
        astar = AStar(State(54861732), State(12345678), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['right', 'down', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'left', 'up', 'up',
                          'right', 'down', 'left', 'up', 'right', 'right', 'down', 'left', 'down', 'left', 'up',
                          'right', 'up', 'left'])

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
                         ['right', 'up', 'up', 'left', 'left', 'down', 'down', 'right', 'right', 'up', 'left', 'left',
                          'down', 'right', 'right', 'up', 'left', 'up', 'right', 'down', 'left', 'up', 'left', 'down',
                          'down', 'right', 'right', 'up', 'left', 'down', 'right'])

    def testComplexProblemeEuclidian(self):
        initialState = State(867254301)
        goalState = State(123456780)
        astar = AStar(initialState, goalState, "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['left', 'up', 'right', 'up', 'right', 'down', 'down', 'left', 'up', 'up', 'right', 'down',
                          'down', 'left', 'up', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 'down', 'right',
                          'up', 'left', 'up', 'right', 'down', 'right', 'down'])

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
