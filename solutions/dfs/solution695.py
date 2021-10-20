from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        self.num = 0
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    self.helper(grid, i, j)
                    ans = ans if ans > self.num else self.num
                    self.num = 0
        return ans

    def helper(self, grid, i, j):
        """
        判断位置（i,j）是否为陆地
        :return:
        """
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.num += 1
        self.helper(grid, i, j - 1)
        self.helper(grid, i, j + 1)
        self.helper(grid, i + 1, j)
        self.helper(grid, i - 1, j)


if __name__ == '__main__':
    solu = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    cnt = solu.maxAreaOfIsland(grid)
    print(cnt)
