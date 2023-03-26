class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        n -= 1
        while n:
            if n & 3 != 3:
                return False
            n >>= 2
        return True
