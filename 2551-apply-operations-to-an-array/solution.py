class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for i in range(len(nums)):
            if nums[i]!=0:
                ans.append(nums[i])
        new = ans + [0]*nums.count(0)
        return new
        
