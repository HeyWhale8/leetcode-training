'''
上楼梯的复杂版？
如果连续的两位数符合条件，就相当于一个上楼梯的题目，可以有两种选法：
1.一位数决定一个字母
2.两位数决定一个字母
就相当于dp(i) = dp[i-1] + dp[i-2];
如果不符合条件，又有两种情况
1.当前数字是0：
不好意思，这阶楼梯不能单独走，
dp[i] = dp[i-2]
2.当前数字不是0
不好意思，这阶楼梯太宽，走两步容易扯着步子，只能一个一个走
dp[i] = dp[i-1];

'''


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] == "0":
            return 0
        if len(s) < 2:
            return 1
        dp[0] = 1
        if int(s[0:2]) < 27:
            if s[1] != "0":
                dp[1] = 2
            else:
                dp[1] = 1
        else:
            if s[1] != "0":
                dp[1] = 1
            else:
                dp[1] = 0

        for idx in range(2, len(s)):
            # 两个数字
            if int(s[idx - 1:idx + 1]) < 27 and s[idx - 1] != "0":
                cur_t = 1
            else:
                cur_t = 0
            cur_o = 0 if s[idx] == "0" else 1
            print("idx = {},elem = {},cur_t = {},cur_o = {}".format(idx, s[idx], cur_t, cur_o))
            dp[idx] = dp[idx - 1] * cur_o + dp[idx - 2] * cur_t
        print(dp)
        return dp[-1]

    def answer(self, s: str) -> int:

        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


if __name__ == '__main__':
    solu = Solution()
    string = "27"
    res = solu.numDecodings(string)
    print(res)
