# coding=utf-8
from collections import Counter


class PolyaSolver:
    def __init__(self, _width, _height, _n_states):

        self.width = _width
        self.height = _height
        self.n_states = _n_states

    @staticmethod
    def _build_gcd_matrix(_positive_int):
        """
        Builds the gcd matrix for all pairs (x,y) with x,y <= max(_w, _h).

        Args:
            _positive_int (int): a positive integer.

        Returns:
            List[List[int]]: A matrix of GCDs.
        """

        gcd_matrix = [[0 for x in range(_positive_int)] for y in range(_positive_int)]
        for i in range(_positive_int):
            for j in range(i, _positive_int):
                if i == 0 or j == 0:
                    gcd_matrix[i][j] = 1
                    gcd_matrix[j][i] = 1
                elif i == j:
                    gcd_matrix[i][j] = i + 1
                else:
                    gcd_matrix[i][j] = gcd_matrix[i][j - i - 1]
                    gcd_matrix[j][i] = gcd_matrix[i][j - i - 1]
        return gcd_matrix

    @staticmethod
    def _build_factorial_matrix(_positive_int):
        """
        Bottom up, as in Dynamic Programming method to compute factorials of a positive integer.

        Args:
            _positive_int (int): a positive integer.

        Returns:
            List[List[int]]: A matrix of Factorials.
        """

        factorials = [1]
        for i in range(_positive_int - 1):
            factorials.append(factorials[-1] * (i + 2))
        return factorials

    @staticmethod
    def _get_all_partitions(_positive_int):
        """
        A recursive algorithm to generate all partitions of a positive integer n.

        Args:
            _positive_int (int): a positive integer.

        Returns:
            List[List[int]]: A matrix of all partitions of a positive integer n.
        """

        def _all_partitions(n, _i=1):
            yield (n,)
            for i in range(_i, n // 2 + 1):
                for p in _all_partitions(n - i, i):
                    yield (i,) + p

        return _all_partitions(_positive_int)

    @staticmethod
    def _get_cycle_index(_positive_int, _positive_int_partitions, _positive_int_factorial_matrix):
        """
        Computes the number of cycles of length k in the cycle decomposition of the permutation g.

        Args:
            _positive_int (int): a positive integer.
            _positive_int_partitions (List[List[int]]): all partitions of a positive integer.
            _positive_int_factorial_matrix (List[List[int]]): A matrix of factorials of a positive integer.

        Returns:
            List[List[int]]: A matrix of Factorials.
        """
        cycle = _positive_int_factorial_matrix[_positive_int - 1]
        for a, b in Counter(_positive_int_partitions).items():
            cycle //= (a ** b) * _positive_int_factorial_matrix[b - 1]
        return cycle

    def solve(self):
        """
        A builder method to execute all steps of the algorithm in order.

        Returns:
            str: number of orbits.
        """

        greater_dimension = max(self.width, self.height)
        gcd_matrix = self._build_gcd_matrix(greater_dimension)
        factorial_matrix = self._build_factorial_matrix(greater_dimension)

        partitions_sigma = 0

        for partitions_w in self._get_all_partitions(self.width):
            permutation_cycle_w = self._get_cycle_index(self.width, partitions_w, factorial_matrix)

            for partitions_h in self._get_all_partitions(self.height):
                permutation_cycle_h = self._get_cycle_index(self.height, partitions_h, factorial_matrix)

                cycles_product = permutation_cycle_w * permutation_cycle_h
                gcd_sigma = sum([
                    sum([
                        gcd_matrix[i - 1][j - 1]
                        for i in partitions_w
                    ])
                    for j in partitions_h
                ])
                partitions_sigma += cycles_product * (self.n_states ** gcd_sigma)

        factorials_product = factorial_matrix[self.width - 1] * factorial_matrix[self.height - 1]
        return str(partitions_sigma // factorials_product)
