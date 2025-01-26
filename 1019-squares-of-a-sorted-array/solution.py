class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [x**2 for x in nums]
        l = 0
        r = len(ans)-1
        an = []
        
        while l <= r:
            if ans[r] > ans[l]:
                an.append(ans[r])
                r -= 1
            else:
                an.append(ans[l])
                l += 1
        return an[::-1]


        
            
        
