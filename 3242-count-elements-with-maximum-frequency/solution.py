class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        maxi = float("-inf")
        for i,j in dic.items():
            if j>maxi:
                maxi = j
        sums = 0
        for i,j in dic.items():
            if j==maxi:
                sums+=j
        return sums


        
