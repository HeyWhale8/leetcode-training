from typing import List

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。
你可以认为每种硬币的数量是无限的。
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # dp[i]表示总金额为i的所需要的最小硬币数
        for coin in coins:
            if coin > amount: break
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    ans = solution.coinChange([1, 2, 5], 11)
    print(ans)
