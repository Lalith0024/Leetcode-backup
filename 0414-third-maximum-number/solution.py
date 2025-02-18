class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        set_nums.sort(reverse=True)
        if len(set_nums)>=3:
            return set_nums[2]
        else:
            return max(set_nums)
            

        
