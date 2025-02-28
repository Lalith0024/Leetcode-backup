class Solution(object):
    def findMin(self, nums):
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     if nums[0]>nums[1]:
        #         return nums[1]
        #     else:
        #         return nums[0]
        # if len(nums)==3:
        #     return min(nums)
        
        # else:
        #     h = len(nums)-1
        #     l = 0
        #     mid = (h+l)//2
        #     min1 = nums[mid]>nums[l]
        #     min2=nums[mid]>nums[h]
        #     if min1>min2:
        #         return nums[0]
        #     else:
        #         return nums[mid+1]

        return min(nums)
            

                    
        
        
