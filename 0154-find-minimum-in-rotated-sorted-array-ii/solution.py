class Solution(object):
    
    def findMin(self, nums):
        l, h = 0, len(nums) - 1

        while l < h:
            mid = (l + h) // 2

            if nums[mid] > nums[h]:  
                l = mid + 1  
            elif nums[mid] < nums[h]:  
                h = mid  
            else:  
                h -= 1  

        return nums[l]

        
