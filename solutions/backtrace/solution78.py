from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums: List[int], trace: List[int], start):
            res.append(trace.copy())
            for i in range(start, len(nums)):
                # 做选择
                trace.append(nums[i])
                backtrace(nums, trace, i + 1)
                # 撤销选择
                trace.pop()

        res = []
        backtrace(nums, [], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.subsets([1,2,3])
    print(res)
