class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        var = nums[len(nums)-k]
        return var
