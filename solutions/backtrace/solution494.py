from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0

        def backtrace(index, sum):
            print("index = {},len(nums) = {}, sum = {}".format(index, len(nums), sum))

            if index == len(nums):
                if sum == target:
                    self.ans += 1
                return
            else:
                backtrace(index + 1, sum=sum + nums[index])
                backtrace(index + 1, sum=sum - nums[index])

        backtrace(0, 0)
        return self.ans


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 1]
    target = 3
    res = solu.findTargetSumWays(nums, target)
    print(res)
