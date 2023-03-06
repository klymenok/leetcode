from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            _item = list(item)
            _item.sort()
            res[tuple(_item)] = res.get(tuple(_item), [])
            res[tuple(_item)].extend([item])
        return list(res.values())
