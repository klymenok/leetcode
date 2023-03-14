class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ''
        return self.convertToTitle((columnNumber - 1) // 26) + chr((columnNumber - 1) % 26 + 65)


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(53))