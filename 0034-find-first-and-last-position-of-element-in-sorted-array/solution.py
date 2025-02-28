class Solution(object):
    def searchRange(self, nums, target):
        res = [-1,-1]
        if target not in nums:
            return res
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (h+l)//2
            if nums[mid]>=target:
                
                res[0] = mid
                h = mid-1
            else:
                l = mid+1
        
                
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (h+l)//2
            if nums[mid]<=target:
                res[1] = mid
                l = mid+1
            else:
                h = mid-1
        
        return res

        

        
