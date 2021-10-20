# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrace(trace, start):
            # print(len(trace), sum(trace), k, n)
            if len(trace) == k and sum(trace) == n:
                res.append(trace.copy())
                return
            if sum(trace) > n:
                return
            for i in range(start, 10):
                trace.append(i)
                backtrace(trace, i + 1)
                trace.pop()
                # print(trace)
                
        res = []
        backtrace([], 1)

        return res


if __name__ == '__main__':
    solution = Solution()
    res2 = solution.combinationSum3(3, 18)
    print(res2)
