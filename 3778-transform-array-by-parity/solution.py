class Solution(object):
    def transformArray(self, nums):
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1  

        bholu, golu = 0, len(nums) - 1
        while bholu < golu:
            while bholu < golu and nums[bholu] == 0:
                bholu += 1
            while bholu < golu and nums[golu] == 1:
                golu -= 1
            if bholu < golu:
                nums[bholu], nums[golu] = nums[golu], nums[bholu]

        return nums
        
        
        
