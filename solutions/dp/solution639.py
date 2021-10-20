class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] == 0:
            return 0
        if s[0] == "*":
            dp[0] = 9
            if s[1] == "0":
                dp[1] = 2  # 10 20

            elif s[1] == "*":  # 随机
                dp[1] = 96
            else:  # 确定值
                dp[1] = 9  # 组成两个字母
                if int(s[1]) > 6:  # 组成一个字母
                    dp[1] += 1
                else:
                    dp[1] += 2
        else:
            dp[0] = 1
            if s[1] == "*":  # 随机
                # 组成两个字母9种，组成一个字母分类讨论
                dp[1] = 9
                if int(s[0]) > 2:
                    dp[1] += 0
                elif int(s[0]) == 1:  # 11-19
                    dp[1] += 9
                else:  # 21-26
                    dp[1] += 6

            else:  # 确定值
                dp[1] = 1  # 组成两个字母
                if int(s[0:2]) < 27:
                    dp[1] += 1
                else:
                    dp[1] += 0
        for idx in range(2, len(s)):
            # 剩下两个数字
            if s[idx - 1] == "0":
                dp2 = dp[idx - 2]
            elif s[idx - 1] == "*":
                if s[idx] == "0":
                    dp2 = 2 * dp[idx]
                elif s[idx] == "*":
                    dp2 = 96 * dp[idx]
                else:
                    # 组成两个字母
                    base = 9
                    # 组成一个字母
                    if int(s[idx]) > 6:
                        dp2 = (base + 1) * dp[idx]
                    else:
                        dp2 = (base + 2) * dp[idx]
            else:
                if s[idx] == "*":  # 随机
                    # 组成两个字母9种，组成一个字母分类讨论
                    dp2 = 9
                    if int(s[idx - 1]) > 2:
                        dp2 += 0
                    elif int(s[idx - 1]) == 1:  # 11-19
                        dp2 += 9
                    else:  # 21-26
                        dp2 += 6
                    dp2 = dp2 * dp[idx - 2]
                else:  # 确定值
                    dp2 = 1  # 组成两个字母
                    if int(s[idx - 1:idx + 1]) < 27:
                        dp2 += 1
                    else:
                        dp2 += 0
                    dp2 += dp[idx - 2]
            # 剩下一个个数字
            if s[idx] == "0":
                dp1 = dp[idx - 1]
            elif s[idx] == "*":
                dp1 = 9 * dp[idx - 1]
            else:
                dp1 = 1 + dp[idx - 1]

            dp[idx] = dp2 + dp1
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    res = solution.numDecodings("123456")
    print(res)
