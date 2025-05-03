
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        max_score = 0   # to record the maximum score
        l = 0   # left pointer
        dupes = set()   # set to hold visited elements
        total = 0   # total sum upto rth element

        for r in range(len(nums)):
            total += nums[r]    # add the rth element to the total

            if nums[r] in dupes:    # check if rth element already in dupes 
                max_score = max(max_score, total-nums[r])   # if yes, save the max score upto but not including the rth element

                while nums[r] in dupes:
                    dupes.remove(nums[l])   # remove the lth element for the set
                    total -= nums[l]    # remove the lth element from the total as well
                    l += 1  # increment left pointer
                
            dupes.add(nums[r])  # add rth element to the set

        return max(max_score, sum(dupes))   # return the max total
