"""
给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0] + 1
        for price in prices:
            if price < buy:
                buy = price  # 计算左起最小价格
            else:
                profit = max(profit, price - buy)  # 计算利润，并随购买价格动态更新
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        cur_sum = 0
        # cur_sum > 0 则在当前卖出能得到的利润 cur_sum < 0 说明有更低的买入点，
        for i in range(1, len(prices)):
            cur_sum += prices[i] - prices[i - 1]
            if cur_sum < 0:
                cur_sum = 0
            # else:
            #     profit = max(profit,cur_sum)
            if cur_sum > profit:
                profit = cur_sum
        return profit


if __name__ == '__main__':
    prices = [2, 9, 1, 7]
    solution = Solution()
    ans = solution.maxProfit(prices)
    print(ans)
    ans = solution.maxProfit2(prices)
    print(ans)
