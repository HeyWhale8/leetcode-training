from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == "1":
                    self.num += 1
                    self.dfs(i, j)
        return self.num

    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]):
            return
        if self.grid[i][j] == "0":
            return
        else:
            self.grid[i][j] = "0"
            self.dfs(i, j - 1)
            self.dfs(i, j + 1)
            self.dfs(i + 1, j)
            self.dfs(i - 1, j)


if __name__ == '__main__':
    solu = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    cnt = solu.numIslands(grid)
    print(cnt)
