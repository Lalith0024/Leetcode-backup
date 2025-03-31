from typing import List

class Solution:
    def rec(self, r: int, c: int, m: int, n: int, grid: List[List[int]], dp: List[List[int]]) -> int:
        if r == m and c == n:
            return grid[r][c]
        if dp[r][c] != -1:
            return dp[r][c]

        right = float('inf')
        down = float('inf')
        
        if c + 1 <= n:
            right = self.rec(r, c + 1, m, n, grid, dp)
        if r + 1 <= m:
            down = self.rec(r + 1, c, m, n, grid, dp)

        dp[r][c] = grid[r][c] + min(right, down)
        return dp[r][c]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return self.rec(0, 0, m - 1, n - 1, grid, dp)
