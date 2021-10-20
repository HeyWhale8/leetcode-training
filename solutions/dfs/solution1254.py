from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        num = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 0:
                    if self.helper(grid, i, j):
                        num += 1

        return num

    # 判断当前位置是否为封闭岛屿
    def helper(self, grid, i, j) -> bool:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            # 已经DFS到边界之外，不满足封闭
            return False
        if grid[i][j] == 1:
            # 边界存在海水
            return True
        grid[i][j] = 1
        a = self.helper(grid, i, j - 1)
        b = self.helper(grid, i, j + 1)
        c = self.helper(grid, i + 1, j)
        d = self.helper(grid, i - 1, j)
        return a and b and c and d


if __name__ == '__main__':
    solu = Solution()
    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    cnt = solu.closedIsland(grid)
    print(cnt)
