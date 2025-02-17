class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        if all(i>0 for i in nums):
            return 1
        elif all(j>0 for j in prefix):
            return 1
        else:
            return abs(min(prefix))+1
            
