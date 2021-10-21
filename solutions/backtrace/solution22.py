from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrace(left, right, trace):
            if left > right: return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(trace)
                return
            trace += "("
            backtrace(left - 1, right, trace)
            trace = trace[0:-1]

            trace += ")"
            backtrace(left, right - 1, trace)
            # trace = trace[0:-1]

        res = []
        trace = ""
        backtrace(n, n, trace)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)
