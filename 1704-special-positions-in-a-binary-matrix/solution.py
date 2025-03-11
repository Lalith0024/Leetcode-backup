class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n=len(mat[0])
        row = []
        col =[]
        for r in mat:
            row.append(sum(r))

        for c in range(n):
            sums=0
            for r in range(m):
                sums+= mat[r][c]
            col.append(sums)

        freq =0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    freq+=1
        return(freq)
        
