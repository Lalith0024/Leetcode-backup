class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums)-1
        lst = [0]*len(nums)
        p = len(lst)-1
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                lst[p] = nums[j]**2
                j-=1

            else:
                lst[p]=nums[i]**2
                i+=1
            p-=1
        return lst

        
        
