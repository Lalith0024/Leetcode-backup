class Solution(object):
    def canJump(self, nums):
        maxi_idx = 0
        for i in range(len(nums)):
            if i>maxi_idx:
                return False
            maxi_idx = max(maxi_idx,(i+nums[i]))
        return True
        #try with recursion
