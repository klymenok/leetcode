class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Last and First indexes
        start = 0
        end = len(nums) - 1
        # Traverse an array
        while (start <= end):
            mid = (start + end)//2
            # if target value found.
            if nums[mid] == target:
                return mid
            # If target value is greater then mid elements's value
            elif target > nums[mid]:
                start = mid + 1
            # otherwise target value is less,
            else:
                end = mid -1
        # Return the insertion position
        return end + 1

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    target = 10
    print(s.searchInsert(nums, target))