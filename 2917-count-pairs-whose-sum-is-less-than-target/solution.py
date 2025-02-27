class Solution(object):
    def countPairs(self, nums, target):
        l = 0
        r = 1
        count = 0
        while l <= len(nums) - 2:
            if r == len(nums):
                l += 1
                r = l + 1
            if r < len(nums) and nums[l] + nums[r] < target:
                count += 1
            r += 1
        return count

        
