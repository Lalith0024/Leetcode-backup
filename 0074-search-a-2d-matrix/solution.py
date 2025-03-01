class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        h = (m*n)-1
        l = 0
        while l<=h:
            mid = (l+h)//2
            row = mid//m
            col = mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                h = mid-1
            else:
                l = mid+1
        return False 
                
