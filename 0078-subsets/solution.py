class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = []
        ans = []
        def rec(nums,lst,i=0):
            if i==len(nums):
                ans.append(lst[:])
                return
            rec(nums,lst,i+1)
            lst.append(nums[i])
            rec(nums,lst,i+1)
            lst.remove(nums[i])
            
            return ans
        return rec(nums,lst)
        
