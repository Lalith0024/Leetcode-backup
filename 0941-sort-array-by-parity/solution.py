class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddarr =[]
        evenarr =[]
        for i in nums:
            if i%2==0:
                evenarr.append(i)
            else:
                oddarr.append(i)
        return evenarr+oddarr        
