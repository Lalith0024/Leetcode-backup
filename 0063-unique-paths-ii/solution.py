class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)        # rows
        m = len(obstacleGrid[0])     # columns
        
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def f(row, col):
            # out of bounds or obstacle
            if row >= n or col >= m or obstacleGrid[row][col] == 1:
                return 0
            
            # reached destination
            if row == n-1 and col == m-1:
                return 1
            
            if dp[row][col] != -1:
                return dp[row][col]
            
            down = f(row + 1, col)
            right = f(row, col + 1)
            
            dp[row][col] = down + right
            return dp[row][col]
        
        return f(0, 0)

