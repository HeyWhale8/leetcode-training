from typing import List


# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(trace: List[int], start):
            prev = 1024
            res.append(trace.copy())
            for i in range(start, len(nums)):
                if nums[i] == prev:
                    continue
                # 做选择
                trace.append(nums[i])
                backtrace(trace, i + 1)
                # 撤销选择
                trace.pop()
                prev = nums[i]

        res = []
        nums.sort()
        backtrace([], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.subsetsWithDup([1, 2, 2])
    print(res)
