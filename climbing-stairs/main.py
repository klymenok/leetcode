class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i, j = 1, 2
        for _ in range(3, n + 1):
            i, j = j, i + j
        return j
