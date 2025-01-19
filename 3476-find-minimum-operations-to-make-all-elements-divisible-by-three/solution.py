class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
    
    
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                ops+=1
            elif remainder == 2:
                ops += 1 
        
        return ops

        
