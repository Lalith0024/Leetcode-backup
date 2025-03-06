class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        maxi = 0  

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            maxi = max(maxi, curr)
            if height[l] < height[r]:
                l += 1  
            else:
                r -= 1  

        return maxi  
        
