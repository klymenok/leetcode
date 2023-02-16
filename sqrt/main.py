class Solution:
    def mySqrt(self, x: int) -> int:
        n = x
        while True:
            root = 0.5 * (n + (x / n))
            if abs(root - n) < 0.1:
                break
            n = root
        return abs(root)
