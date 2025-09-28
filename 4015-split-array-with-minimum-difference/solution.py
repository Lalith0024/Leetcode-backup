class Solution:
    def splitArray(self, nums: List[int]) -> int:
        # left is increasing? that means sorted ig.. 
        # wait the meaning tells if exists -> that means some dont overthing about it. 
        # right should be decreasing -> reverse sorted thing got it 

        plo = nums[:]
        n = len(nums)

        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]
        increasing = [True]*n
        for i in range(1,n):
            increasing[i] = increasing[i-1] and nums[i]>nums[i-1]

        decreasing = [True]*n
        for i in range(n-2,-1,-1):
            decreasing[i] = decreasing[i+1] and nums[i]>nums[i+1]

        ans = float('inf')
        for i in range(n-1):
            if increasing[i] and decreasing[i+1]:
                left_sum = prefix[i + 1] 
                right_sum = prefix[n] - prefix[i + 1] 
                ans = min(ans, abs(left_sum - right_sum))

        return -1 if ans == float("inf") else ans

    







