from typing import List

class Solution:
    def rob(self,nums: List[int]) -> int:
        if len(nums)<2:
            return max(nums)
        rob_cur = 0
        hop_cur = 0
        for i in range(1,len(nums)):
            item = nums[i]
            # if rob current value, previous house must not be robbed
            temp = hop_cur + item
            # if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            hop_cur = max(hop_cur, rob_cur)
            rob_cur = temp
        dp1 = max(hop_cur, rob_cur)
        rob_cur = 0
        hop_cur = 0
        for i in range(len(nums)-1):
            # hop last one:
            item = nums[i]
            temp = hop_cur + item
            # if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            hop_cur = max(hop_cur, rob_cur)
            rob_cur = temp
        dp2 = max(hop_cur, rob_cur)
        return max(dp1, dp2)

if __name__ == '__main__':
    solution = Solution()
    res = solution.rob([1])
    print(res)
