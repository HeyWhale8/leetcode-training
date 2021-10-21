from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 5]
    res = solu.minMoves(nums)
    print(res)
