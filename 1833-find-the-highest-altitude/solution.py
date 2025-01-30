class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_gain = current
        for i in range(len(gain)):
            current+=gain[i]
            max_gain = max(max_gain,current)   
        return max_gain     
