class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        neg = not ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0))
        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor

        res = 0
        for b in range(31, 0, -1):
            if divisor << b <= dividend:
                res += 2 ** b
                dividend -= divisor << b
        res += int(dividend >= divisor)
        return -res if neg else res
