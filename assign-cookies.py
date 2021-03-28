from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    # 孩子
        s.sort()    # 饼干
        # print(g)
        # print(s)
        num = 0
        j = 0
        for i in range(len(s)):
            if j < len(g) and g[j] <= s[i]:
                num += 1
                j += 1
        return num