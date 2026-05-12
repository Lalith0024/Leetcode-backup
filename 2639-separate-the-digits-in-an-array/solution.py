class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            for j in str(i):
                arr.append(int(j))
        return arr
