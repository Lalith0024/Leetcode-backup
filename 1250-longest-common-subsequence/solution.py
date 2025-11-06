class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        def f(a,b):
            if a>=n or b>=m:
                return 0
            if text1[a] == text2[b]:
                return 1 + f(a+1,b+1)
            if dp[a][b]!=-1:
                return dp[a][b]
            one_step = f(a+1,b)
            two_step = f(a,b+1)
            dp[a][b] = max(one_step,two_step)
            return dp[a][b]
        return f(0,0)


