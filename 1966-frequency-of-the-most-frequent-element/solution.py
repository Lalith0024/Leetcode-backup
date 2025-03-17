class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0

        for r in range(len(nums)):
            total += nums[r]
            while nums[r]*(r-left+1)>total+k:
                total -= nums[left]
                left += 1
            max_freq = max(max_freq,r-left+1)
        return max_freq
        
