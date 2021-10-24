from typing import List

"""
皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的n皇后问题 的解决方案。
每一种解法包含一个不同的n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []

        def backtrace(board, row):
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)

                return
            for col in range(n):
                if meet(board, row, col):
                    board[row][col] = 'Q'
                    backtrace(board, row + 1)
                    board[row][col] = '.'

        def meet(board, row, col):
            for i in range(n):
                if board[i][col] == "Q":
                    return False
            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        backtrace(board, 0)
        return res
if __name__ == '__main__':
    solution = Solution()
    ans = solution.solveNQueens(4)
    print(ans)