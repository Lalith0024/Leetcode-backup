class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = len(nums), -1
        si, ei = 0, len(nums)-1

        while si <= ei:
            mid = (si + ei) >> 1
            if nums[mid] < 0:
                neg = mid
                si = mid + 1
            elif nums[mid] >= 0:
                ei = mid - 1
        
        si, ei = 0, len(nums)-1
        while si <= ei:
            mid = (si + ei) >> 1
            if nums[mid] > 0:
                pos = mid
                ei = mid - 1
            elif nums[mid] <= 0:
                si = mid + 1
        #print((neg+1), (len(nums)-pos))
        return max((neg+1), (len(nums)-pos))
