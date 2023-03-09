from typing import List


class Solution:

    def _permute(self, k, nums, res):
        if k == 1:
            res.append(nums.copy())
        else:
            self._permute(k - 1, nums, res)
            for i in range(k - 1):
                nums[0 if k % 2 else i], nums[k -1] = nums[k - 1], nums[0 if k % 2 else i]
                self._permute(k - 1, nums, res)


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._permute(len(nums), nums, res)
        return res
