class Solution(object):
    def search(self, nums, target):
        l = 0
        h = len(nums)-1
        while l<=h:
            mid = (h+l)//2
            if nums[mid]==target:
                return mid
            if nums[l]>nums[mid]:
                if nums[mid] < target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
            else:
                if nums[l] <= target < nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
        return -1

        
