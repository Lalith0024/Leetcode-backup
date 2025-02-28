class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        l,h=0,len(nums)-1
        left=right=-1
        while l<=h: 
            m=(l+h)>>1
            if nums[m]==target:
                left=m
                h=m-1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        l,h=left,len(nums)-1
        while l<=h: 
            m=(l+h)>>1
            if nums[m]==target:
                right=m
                l=m+1
            elif nums[m]>target:
                h=m-1
            else:
                l=m+1
        if left==-1:
            return []
        ans=range(left,right+1)
        return ans   
        
        
