class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        else:
            nums.sort()
            maxi = 0

            for i in range(1,len(nums)):
                if (nums[i]-nums[i-1])>maxi:
                    maxi = nums[i]-nums[i-1]
        return maxi

        
