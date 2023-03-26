class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = ''
        while s:
            min_unique = min(map(s.rindex, set(s)))
            min_char = min(s[:min_unique + 1])
            res += min_char
            s = s[s.index(min_char):].replace(min_char, '')
        return res
