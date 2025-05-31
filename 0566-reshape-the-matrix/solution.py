
class Solution(object):
    def matrixReshape(self, mat, r, c):

        if not mat: return mat
       
        if len(mat) * len(mat[0]) != r * c:
            return mat
       
        output = [[0 for i in range(c)] for i in range(r)]
        idx = 0
        
        while idx < r * c:
            
            output[idx // c][ idx % c] =  mat[idx // len(mat[0])][idx % len(mat[0])]
            idx += 1
        return output       # Return the output matrix...
