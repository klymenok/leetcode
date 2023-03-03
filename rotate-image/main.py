from pprint import pprint
from typing import List


class Solution:
    def swap(self, shift, index, matrix, end):
        pass

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix) - 1
        for shift in range(l // 2 + 1):
            for i in range(l - (shift * 2)):
                (matrix[shift][shift + i],
                 matrix[shift + i][l - shift],
                 matrix[l - shift][l - shift - i],
                 matrix[l - shift - i][shift]) = \
                (matrix[l - shift - i][shift],
                 matrix[shift][shift + i],
                 matrix[shift + i][l - shift],
                 matrix[l - shift][l - shift - i])
