class Solution:
    def countCollisions(self, directions: str) -> int:
        # at each index there are L , R , S
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        
        ans = 0
        for c in directions:
            if c != "S":
                ans += 1
        return ans
