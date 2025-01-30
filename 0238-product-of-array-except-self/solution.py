class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answer = []
        count = 0

        for i in nums:
            if i == 0:
                count += 1
            else:
                product *= i
        
        if count == 0:
            for i in range(len(nums)):
                answer.append(product//nums[i]) 
        elif count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    answer.append(product)
                else:
                    answer.append(0)
        else:
            return [0]*len(nums)
        
        return answer

        
