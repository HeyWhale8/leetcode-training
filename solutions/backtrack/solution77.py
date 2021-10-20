from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(max: int, num: int, start, trace: List[int]):
            # 将path添加到res结果中
            if len(trace) == num:
                res.append(trace.copy())
                return
            for i in range(start, max + 1):
                # 做选择
                trace.append(i)
                backtrack(max, num, i + 1, trace)
                # 撤销选择
                trace.pop()

        res = []
        backtrack(n, k, 1, [])

        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.combine(4, 2)
    print(res)
