class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        
        for i in range(n):
            s += mat[i][i]            
            s += mat[i][n - 1 - i]     
        
        
        if n % 2 == 1:
            s -= mat[n // 2][n // 2]
        
        return s

