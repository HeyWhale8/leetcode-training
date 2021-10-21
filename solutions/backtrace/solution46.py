from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(nums, path, length):
            # 将path添加到res结果中
            if len(path) == length:
                res.append(path.copy())
            for i in range(len(nums)):
                nums_copy = nums.copy()
                nums_copy.remove(nums[i])
                # 做选择
                path.append(nums[i])
                backtrace(nums_copy, path, length)
                # 撤销选择
                path.pop()

        res = []
        backtrace(nums, [], len(nums))

        return res





if __name__ == '__main__':
    solution = Solution()
    res = solution.permute([1, 2, 3])
    print(res)
