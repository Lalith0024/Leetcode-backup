class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        var1 = 0
        var2 = 0

        for i in nums[: -1]:
            temp = var1
            var1 = max(var2 + i, var1)
            var2 = temp

        vaar1 = 0
        vaar2 = 0

        for i in nums[1 : ]:
            temp = vaar1
            vaar1 = max(vaar2 + i, vaar1)
            vaar2 = temp
        return max(var1, vaar1)

        
