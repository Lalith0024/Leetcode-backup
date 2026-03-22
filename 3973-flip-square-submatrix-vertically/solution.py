class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # edge cases?
        # what if k exceeds the whole mat?
        # its mentioned in constraints it wont exceed and x, y are both within the matrix out of bounds so no need      to                   handlecases for this lets proceed with the solution 

        # constraints - > 50 , can go with nested loops approach 

        # input. ->  grid , x = row , y = col index , k = side length

        # task = flip the submatrix by reversing the order of its rows vertically 


        # simply they are telling to flip it 180 degrees 

        for i in range(k // 2):
            # top_row is the index of the row at the top of our "swap" pair
            top_row = x + i
            # bottom_row is the index of the row at the bottom of our "swap" pair
            bottom_row = x + k - 1 - i
            
            # Now, only swap the numbers in the columns belonging to the submatrix
            # These columns start at 'y' and go for 'k' steps
            for j in range(y, y + k):
                # Standard swap logic: a, b = b, a
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
                
        return grid

