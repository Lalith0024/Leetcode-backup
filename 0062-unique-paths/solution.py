class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        def f(row,col):
            if row<0 or col<0 or row>m-1 or col>n-1:
                return 0
            if row == m-1 and col == n-1:
                return 1

            if dp[row][col]!=-1:
                return dp[row][col]
            
            down = f(row+1,col)
            right = f(row,col+1)
            dp[row][col] = down+right
            return dp[row][col]
        return f(0,0)



            
            


