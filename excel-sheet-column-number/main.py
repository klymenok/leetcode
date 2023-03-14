class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if len(columnTitle) == 1:
            return ord(columnTitle[0]) - 64
        else:
            return self.titleToNumber(columnTitle[1:]) + (ord(columnTitle[0]) - 64) * (26 ** (len(columnTitle) - 1))
