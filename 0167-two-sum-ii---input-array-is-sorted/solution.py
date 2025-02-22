class Solution(object):
    def twoSum(self, numbers, target):
        high  = len(numbers)-1
        low = 0
        while low<=high:
            total = numbers[high]+numbers[low]
            if total == target:
                return low+1,high+1
            if total>target:
                high-=1
            else:
                low+=1
        
