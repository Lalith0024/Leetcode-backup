class Solution(object):
    def findChampion(self, grid):
        row = []
        maxi = 0
        for row2 in range(len(grid)):
            maxi = max(maxi,sum(grid[row2]))
            row.append(sum(grid[row2]))
        return(row.index(maxi))
        
                

        

