class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # given conditions 
        # 1st -> arr[0]<arr[... upto p]
        # 2nd -> arr[p]>arr[... upto q]
        # 3rd -> arr[q]<arr[..upto len(arr)]

        # basically we need an o(n) solution because we need to check everything related to it and prove weather its an tri thing or not

        if len(nums)==3:
            return False
        
        # constraints are 100 so most prob expect for re lookup 
        # hint -> use peak and valley kind of thing 
        # but how to identify the p, q? should we consider the first occueence and keep it updating??   
        p, q = 0, 0
        
        for i in range(1, len(nums)):
            if p == 0:
                if nums[i] > nums[i-1]:
                    continue # Still climbing
                elif nums[i] < nums[i-1]:
                    if i == 1: return False # Never climbed
                    p = i - 1 # Peak found
                else: 
                    return False # Duplicate = Fail
            
            # 2. Dropping to q
            elif q == 0:
                if nums[i] < nums[i-1]:
                    continue # Still dropping
                elif nums[i] > nums[i-1]:
                    q = i - 1 # Valley found
                else: 
                    return False # Duplicate = Fail
                
            # 3. Final climb
            else:
                if nums[i] <= nums[i-1]: # Must be strictly increasing
                    return False

        return p != 0 and q != 0
            







