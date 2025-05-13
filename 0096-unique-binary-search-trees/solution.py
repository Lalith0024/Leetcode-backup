class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)

        for node in range(2, n + 1):
            dp[node] = 0
            for i in range(1, node + 1):
                dp[node] += dp[i - 1] * dp[node - i]
        
        return dp[n]
