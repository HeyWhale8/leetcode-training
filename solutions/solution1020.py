from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        self.num = 0
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    if self.helper(grid, i, j):
                        ans += self.num
                        print("({},{}) add num:{}".format(i, j, self.num))

                    self.num = 0

        return ans

    def helper(self, grid, i, j) -> bool:
        '''
        判断位置（i,j）是否为enclave
        :return:满足enclave条件则返回True
        '''
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            # 已经DFS到边界之外，不满足
            return False
        if grid[i][j] == 0:
            # 边界存在海水
            return True
        grid[i][j] = 0
        self.num += 1
        a = self.helper(grid, i, j - 1)
        b = self.helper(grid, i, j + 1)
        c = self.helper(grid, i + 1, j)
        d = self.helper(grid, i - 1, j)
        res = a and b and c and d

        return res


if __name__ == '__main__':
    solu = Solution()
    grid =[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    cnt = solu.numEnclaves(grid)
    print(cnt)
