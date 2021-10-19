from typing import List





class Solution:
    def rob(self,nums: List[int]) -> int:
        rob_cur = 0
        hop_cur = 0
        for item in nums:
            # if rob current value, previous house must not be robbed
            temp = hop_cur + item
            # if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            hop_cur = max(hop_cur, rob_cur)
            rob_cur = temp
        return max(hop_cur, rob_cur)


if __name__ == '__main__':
    solution = Solution()
    res = solution.rob([1, 2, 3, 4, 23, 423, 1])
    print(res)
