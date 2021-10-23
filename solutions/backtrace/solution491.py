from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(trace, start):
            print(trace, start)
            prev = 1024
            if len(trace) > 1:
                res.append(trace.copy())
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                if nums[i] == prev: continue
                if len(trace) > 0 and trace[-1] > nums[i]:
                    continue

                trace.append(nums[i])
                backtrace(trace, i + 1)
                trace.pop()
                prev = nums[i]

        backtrace([], 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
    print(ans)
