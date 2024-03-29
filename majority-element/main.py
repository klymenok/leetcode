from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in set(nums):
            if nums.count(num) > len(nums) // 2:
                return num
