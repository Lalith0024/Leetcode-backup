class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        c = 0
        for i in range(len(nums)):
            if nums[i]>median:
                c+= nums[i]-median
            else:
                c+=median-nums[i]
        return c        
        
        
