"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j]。如果 s[j]>= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
"""
from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        for i in range(len(s)):
            if res < len(g) and s[i] >= g[res]:  # 小饼干先喂饱小胃口
                res += 1
        return res

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        start, count = len(s) - 1, 0
        for index in range(len(g) - 1, -1, -1):  # 先喂饱大胃口
            if start >= 0 and g[index] <= s[start]:
                start -= 1
                count += 1
        return count

    def findContentChildren3(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        start = 0
        for i in range(len(g)):
            for j in range(start, len(s)):
                if s[j] >= g[i]:
                    res += 1
                    start = j + 1

                    break
        return res


if __name__ == '__main__':
    solution = Solution()
    g = [1,2,3]
    s = [1,1]
    ans = solution.findContentChildren3(g, s)
    print(ans)
