"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i]：i的完全平方数的最少数量为dp[i]
        dp = [n] * (n + 1)
        dp[0] = 0
        # 遍历背包
        for j in range(1, n + 1):
            for i in range(1, n):
                num = i ** 2
                if j >= num:
                    dp[j] = min(dp[j], dp[j - num] + 1)
                else:
                    break
        return dp[n]

    def numSquares2(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n):

            num = i * i
            if num > n: break
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]
