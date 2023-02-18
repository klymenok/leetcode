from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(filter(lambda x: x > 0, nums))
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1
