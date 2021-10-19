class Solution:
    def fib(self, n: int) -> int:
        fibonacci = [0, 1]
        if n < 2:
            return n
        for i in range(2, n + 1):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        return fibonacci[-1]


if __name__ == '__main__':
    a = Solution()
    fib= a.fib(30)
    print(fib)
