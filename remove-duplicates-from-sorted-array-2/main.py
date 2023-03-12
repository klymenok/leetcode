from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first, second = 2, 2
        while second < len(nums):
            if nums[first - 2] != nums[second]:
                nums[first] = nums[second]
                first += 1
            second += 1
        return first
