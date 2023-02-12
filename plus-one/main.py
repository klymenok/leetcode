from typing import List


class Solution:
    add = False

    def plusOne(self, digits: List[int], n=-1) -> List[int]:
        if digits[n] == 9:
            if len(digits[:n]) == 0:
                digits[n] = 1
                self.add = True
            else:
                self.plusOne(digits, n - 1)
                digits[n] = 0
        else:
            digits[n] += 1
        if n == -1 and self.add:
            digits.append(0)
        return digits
