"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = prices[0]
        buy2 = prices[0]
        profit1 = 0
        profit2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)

            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            print("Current Price:{}, Hold1:{}, Release1:{}, Hold2:{}, Release2:{}"
                  .format(price, buy1, profit1, buy2, profit2))
        return profit2


if __name__ == '__main__':
    solution = Solution()
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [3, 5, 1, 7, 2, 6]
    ans = solution.maxProfit(prices)
    print(ans)

    prices = [2, 6, 1, 7, 3, 5]
    ans = solution.maxProfit(prices)
    print(ans)
