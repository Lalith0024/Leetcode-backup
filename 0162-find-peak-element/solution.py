class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #okay lets do by binary seach 
        high = len(nums)-1
        low = 0
        while low<high:
            mid = (high+low)//2
            if  nums[mid]>nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low     
        
