class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        def f(i):
            # success case
            if i>=n:
                return 1
            # failed case
            if s[i]=="0":
                return 0
            if dp[i]!=-1:
                return dp[i]
            one = f(i+1)
            two = 0
            if i+1<n and 10<= int(s[i:i+2])<=26:
                two = f(i+2)
            dp[i] = one + two
            return dp[i]
        return f(0)

            

