class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # sorted -> can apply binary search 
        # goal is to find something which occurs only once you could go through a brute force solution which is o(n**2) and using a dict 
        # clear specified o(log n), o(1)-> applies binary search makes sense hmmm


        # lets try basic binary search code and make some tweeks to achive the output 

        # binary search 
        n = len(nums)
        start, end = 0,n-1
        
        while start <= end:
            mid = (start + end) // 2
            
            # Check if mid is the single element i mean check its left and right so that it meets the requirments of single elem
            # (Added boundary checks mid == 0 and mid == n-1 so it doesn't crash on edges)
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == n - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            # even odd case just move right side 
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                start = mid + 1 
            else:
                # move left and bring your search space to the left
                end = mid - 1  
        

            
