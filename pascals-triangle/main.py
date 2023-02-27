from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[]]
        j = 1
        for i in range(numRows * (numRows + 1) // 2):
            r = j * (j + 1) // 2
            if i < 4 or i in (r, r - 1):
                res[-1].append(1)
            else:
                index = (i - j) % ((j - 2) * (j - 1) // 2)
                res[-1].append(res[-2][index] + res[-2][index + 1])
            if r == i + 1 and j < numRows:
                res.append([])
            if r == i:
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generate(7))