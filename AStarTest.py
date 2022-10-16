import unittest

from AStar import AStar
from State.State import State


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def testEasyPuzzleManhattan(self):
        astar = AStar(State("125340678"), State("012345678"), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0], ["up", "left", "left"])

    def testEasyPuzzleEuclidian(self):
        astar = AStar(State("125340678"), State("012345678"), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0], ["up", "left", "left"])

    def testSolvePuzzleWithDepth27Manhattan(self):
        astar = AStar(State("054861732"), State("012345678"), "manhattan")
        report = astar.getReport()
        self.assertEqual(report[0], ['down', 'right', 'down', 'left', 'up', 'right', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'right', 'down', 'down', 'left', 'up', 'up', 'right', 'down', 'down', 'left', 'left', 'up', 'up'])

    def testSolvePuzzleWithDepth27Euclidian(self):
        astar = AStar(State("054861732"), State("012345678"), "euclidian")
        report = astar.getReport()
        self.assertEqual(report[0],
                         ['right', 'down', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'left', 'up', 'up', 'right', 'down', 'left', 'up', 'right', 'right', 'down', 'left', 'down', 'left', 'up', 'right', 'up', 'left'])
    # this state is made to dimostrant that a* is better in case of manhattan than euclidian
    # because in bid test cases manhattan hs less expand nodes than euclidian
    def testcompareExpandOfPuzzleWithDepth27ManhattanAndEuclidian(self):
        astarM = AStar(State("054861732"), State("012345678"), "manhattan")
        reportM = astarM.getReport()
        astarD = AStar(State("054861732"), State("012345678"), "euclidian")
        reportD = astarD.getReport()
        self.assertLess(reportM[2], reportD[2])


    def test(self):
        astar = AStar(State("054861732"), State("012345678"))
        report = astar.getReport()
        for i in report:
            print(i)
if __name__ == '__main__':
    unittest.main()
