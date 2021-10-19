from typing import List


# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

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
import torch
torch.zeros()