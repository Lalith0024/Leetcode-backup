class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for i in range(4):
            if mat == target:
                return True
            else:
                for i in range(n):
                    for j in range(i,n):
                        mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            for i in range(n):
                mat[i].reverse()
                
        return False
        
