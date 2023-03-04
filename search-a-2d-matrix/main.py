from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        if matrix[0][0] <= target <= matrix[0][-1]:
            return bool({target} & set(matrix[0]))
        if matrix[-1][0] <= target <= matrix[-1][-1]:
            return bool({target} & set(matrix[-1]))
        l = len(matrix) // 2
        return self.searchMatrix(matrix[:l], target) if matrix[0][0] <= target <= matrix[l - 1][-1] else self.searchMatrix(matrix[l:], target)
