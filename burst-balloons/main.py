class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        l = len(nums)

        st = [[0] * l for _ in range(l - 1)]

        for left in range(l - 2, -1, -1):
            for right in range(left + 2, l):
                st[left][right] = max(nums[left] * nums[middle] * nums[right] + st[left][middle] + st[middle][right] for middle in range(left + 1, right))
        return st[0][-1]
