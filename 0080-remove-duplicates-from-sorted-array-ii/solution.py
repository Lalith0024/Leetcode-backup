class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:     
        same_found = False
        insert_idx = 0
        size = len(nums)

        if size == 1:
            return 1

        for i in range(1, size):
            if nums[i] != nums[i-1]:
                # Current run has ended, so we overwrite at insert_idx with 1 or 2 copies
                if same_found == False:
                    nums[insert_idx] = nums[i-1]
                    insert_idx += 1
                else:
                    nums[insert_idx:insert_idx+2] = nums[i-2:i]
                    insert_idx += 2
                same_found = False
            else:
                # Found a least 1 duplicate in the current run
                same_found = True
            
            # Handle the very last run when we reach the end of the list
            if i == size-1:
                if same_found == False:
                    nums[insert_idx] = nums[i]
                    insert_idx += 1
                else:
                    nums[insert_idx:insert_idx+2] = nums[i-1:i+1]
                    insert_idx += 2

        return insert_idx
