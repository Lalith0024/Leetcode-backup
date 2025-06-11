class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # ✅ Sort to handle duplicates

        def rec(nums, i, temp):
            nonlocal ans
            if i >= len(nums):
                ans.append(temp)
                return

            # ✅ Pick the current element
            rec(nums, i + 1, temp + [nums[i]])

            # ✅ Skip duplicates for not picking
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # ✅ Do not pick the current element
            rec(nums, i + 1, temp)

        rec(nums, 0, [])
        return ans

