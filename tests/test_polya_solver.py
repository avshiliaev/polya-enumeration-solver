import unittest

from src.polya_solver import PolyaSolver


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case_01 = (2, 3, 4, "430")
        self.test_case_02 = (2, 2, 2, "7")

    @staticmethod
    def solution(w, h, s):
        solver = PolyaSolver(w, h, s)
        return solver.solve()

    def test_solution_01(self):
        result = self.solution(self.test_case_01[0], self.test_case_01[1], self.test_case_01[2])
        self.assertEqual(self.test_case_01[3], result)

    def test_solution_02(self):
        result = self.solution(self.test_case_02[0], self.test_case_02[1], self.test_case_02[2])
        self.assertEqual(self.test_case_02[3], result)


if __name__ == '__main__':
    unittest.main()
