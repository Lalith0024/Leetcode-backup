class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # new = []
        # count = 0
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]!=0:
        #         new.append(i)
                
        # return new       
        # l = 0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[l],nums[i]=nums[i],nums[l]
        #         l+=1 #note this 
        # return nums
        count = nums.count(0)  # Count the number of zeros
        nums[:] = [num for num in nums if num != 0] + [0] * count 
       
        

