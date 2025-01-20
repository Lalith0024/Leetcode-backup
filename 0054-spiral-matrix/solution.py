class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right = 0,len(matrix[0])-1
        top,bottom = 0,len(matrix)-1
        l = []
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1 #doubt
            for j in range(top,bottom+1):
                l.append(matrix[j][right])
            right -=1
            for i in range(right,left-1,-1):
                if left<=right and top<=bottom:
                    l.append(matrix[bottom][i])
            bottom -=1
            for i in range(bottom,top-1,-1):
                if left<=right and top<=bottom:
                    l.append(matrix[i][left])
            left +=1
        return l
                
