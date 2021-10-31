"""
给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
返回有给定数组 nums 构建的 最大二叉树 。
"""

from solutions.utils.tree import TreeNode
from typing import List


class Solution:
    def findMaxIndex(self, nums: List[int], start: int, end: int) -> int:
        idx = -1
        max_num = -1
        for i in range(start, end):
            num = nums[i]
            if num > max_num:
                max_num = num
                idx = i
        return idx

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        node = self.helper(nums, 0, len(nums))
        return node

    def helper(self, nums, start: int, end: int):
        if start == end:
            return None
        idx = self.findMaxIndex(nums, start, end)
        root = TreeNode(nums[idx])
        root.left = self.helper(nums, start, idx)
        root.right = self.helper(nums, idx + 1, end)
        return root

if __name__ == '__main__':
    solution = Solution()
    root = solution.constructMaximumBinaryTree(nums=[3, 2, 1])
    print(root)
    print(root.right.val)
