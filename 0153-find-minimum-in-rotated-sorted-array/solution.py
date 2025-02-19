class Solution(object):
    def findMin(self, nums):
        h = len(nums)-1
        l = 0
        
    

        while l < h:
            mid = (l + h) // 2

            if nums[mid] > nums[h]:  
                l = mid + 1  
            else:
                h = mid  

        return nums[l]


        
