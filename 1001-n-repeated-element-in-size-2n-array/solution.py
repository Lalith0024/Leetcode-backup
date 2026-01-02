class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        print(dic)

        for i,j in dic.items():
            if j==n//2:
                return i
                break
        return "not found"

