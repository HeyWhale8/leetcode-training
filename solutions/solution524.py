from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ""

        for i, word in enumerate(dictionary):
            if len(word) > len(s):
                continue
            idx = 0
            j = 0
            while j < len(s) and idx < len(word):
                if s[j] == word[idx]:
                    idx += 1
                j += 1
            if idx == len(word):
                if idx > len(ans):
                    ans = word

                elif idx == len(ans):
                    ans = ans if ans < word else word

        return ans


if __name__ == '__main__':
    solution = Solution()
    res = solution.findLongestWord("abce", dictionary=["abe","abc"])
    print(res)
