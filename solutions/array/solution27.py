from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for num in nums:
            if num == val:
                continue
            else:
                nums[idx] = num
                idx += 1
        return idx


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    ans = solution.removeElement(nums, val)
    print(ans)
