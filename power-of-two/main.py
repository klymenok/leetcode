class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n -= 1
        while n:
            if not n & 1:
                return False
            n >>= 1
        return True
