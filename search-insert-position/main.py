from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def get_index(_nums, index):
            l = len(_nums)
            if l > 1:
                left = _nums[:int(l / 2)]
                right = _nums[int(l / 2):]
                for num in left:
                    if num >= target:
                        return index
                    index += 1
                return get_index(right, index)
            return index + 1 if _nums[0] < target else index
        return get_index(nums, 0)
