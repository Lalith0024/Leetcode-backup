class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(10000)] for _ in range(n)]

        def f(i,curr):
            if i>=n:
                if curr==target:
                    return 1
                return 0
            if dp[i][curr]!=-1:
                return dp[i][curr]
            plus = f(i+1,curr+nums[i])
            minus = f(i+1,curr-nums[i])
            dp[i][curr] = plus + minus
            return dp[i][curr]
        return f(0,0)

