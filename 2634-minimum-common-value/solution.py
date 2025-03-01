class Solution(object):
    def getCommon(self, nums1, nums2):
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):  # Fix: Use < instead of <=
            if nums1[i] == nums2[j]:  # Common element found
                return nums1[i]
            elif nums1[i] < nums2[j]:  # Move i forward
                i += 1
            else:  # Move j forward
                j += 1
        return -1 
