from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        cnt = 0
        chalk_sum = sum(chalk)
        k = k % chalk_sum
        for i in range(len(chalk)):
            cnt += chalk[i]
            if cnt > k: return i


if __name__ == '__main__':
    solution = Solution()
    nums = solution.chalkReplacer([1, 35, 5], 100)
    print(nums)

