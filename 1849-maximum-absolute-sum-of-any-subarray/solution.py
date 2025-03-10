class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        maxi = mini = 0
        
        for num in nums:
            maxi = max(num, maxi + num)
            mini = min(num, mini + num)
            
            max_sum = max(max_sum, maxi)
            min_sum = min(min_sum, mini)
        
        return max(abs(max_sum), abs(min_sum))
        
