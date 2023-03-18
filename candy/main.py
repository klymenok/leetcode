from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        res = [1] * l
        i = 0
        while i < l - 1:
            if ratings[i] < ratings[i + 1]:
                res[i + 1] = max(res[i] + 1, res[i + 1])
            i += 1
        while i > 0:
            if ratings[i] < ratings[i - 1]:
                res[i - 1] = max(res[i - 1], res[i] + 1)
            i -= 1
        return sum(res)
