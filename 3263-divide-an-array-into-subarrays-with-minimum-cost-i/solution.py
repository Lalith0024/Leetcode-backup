class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums)==3:
            return sum(nums)
       
        first = nums[0]

        nums[1:] = sorted(nums[1:])

        return first + nums[1] + nums[2]



