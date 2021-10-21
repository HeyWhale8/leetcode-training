from typing import List

# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
'''
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums, trace):
            prev = 1024
            if length == len(trace):
                res.append(trace.copy())
            for num in nums:
                if num == prev:
                    continue
                trace.append(num)
                nums_copy = nums.copy()
                nums_copy.remove(num)

                backtrace(nums_copy, trace)
                trace.pop()
                prev = num
            return
        length = len(nums)
        res = []
        trace = []
        nums.sort()
        backtrace(nums, trace)
        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [3,3,0,3]
    res = solu.permuteUnique(nums)
    print(res)
