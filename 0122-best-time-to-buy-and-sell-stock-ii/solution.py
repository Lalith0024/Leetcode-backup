class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        def f(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy==1:
                take = -prices[i] + f(i+1,0)
                leave = f(i+1,buy)
                dp[i][buy] = max(take,leave)
                return dp[i][buy]

            else:
                take = prices[i] + f(i+1,1)
                leave = f(i+1,buy)
                dp[i][buy] = max(take,leave)
                return dp[i][buy]
        return f(0,1)


