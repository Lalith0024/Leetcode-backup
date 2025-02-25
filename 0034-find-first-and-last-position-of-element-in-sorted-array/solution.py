class Solution(object):
    def searchRange(self, nums, target):
        ans = [-1,-1]
        l  = 0
        h = len(nums)-1
        res=-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                res = mid
                h = mid-1
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        ans[0]=res
        res2 = -1
        l  = 0
        h = len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                res2 = mid
                l = mid+1
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        ans[1]=res2
        return ans
                
        

        
