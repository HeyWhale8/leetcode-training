from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(trace, start, target):
            prev = 0
            if target == 0:
                res.append(trace.copy())
            if target < 0:
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num == prev:
                    continue
                trace.append(num)
                backtrace(trace, i + 1, target - num)
                trace.pop()
                prev = num

        def backtrace2(trace, start, target):

            if target == 0:
                res.append(trace.copy())
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i-1 >= start and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]

                trace.append(num)
                backtrace(trace, i + 1, target - num)
                trace.pop()

        res = []
        trace = []
        candidates.sort()

        backtrace2(trace, 0, target)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    print(res)
