from typing import List


# 给定一个无重复元素的正整数数组candidates和一个正整数target，找出candidates中所有可以使数字和为目标数target的唯一组合。
# candidates中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。
# 对于给定的输入，保证和为target 的唯一组合数少于 150 个。

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(trace, choice, target):
            if target == 0:
                res.append(trace.copy())
                return
            if target < 0:
                return
            for i, num in enumerate(choice):
                trace.append(num)
                backtrace(trace, choice[i:], target - num)
                trace.pop()

        res = []
        backtrace([], candidates, target)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum(candidates=[2, 3, 6, 7], target=48)
    print(res)
