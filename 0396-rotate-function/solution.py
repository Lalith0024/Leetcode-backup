from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Compute F(0) and total_sum
        F = 0
        total_sum = 0
        for i in range(n):
            F += i * nums[i]
            total_sum += nums[i]
        
        max_val = F
        
        # Compute F(k) for k from 1 to n-1 using the recurrence relation
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            if F > max_val:
                max_val = F
        
        return max_val
        
