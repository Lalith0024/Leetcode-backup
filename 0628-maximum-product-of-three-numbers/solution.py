class Solution:
    def maximumProduct(self, vec: List[int]) -> int:
        if len(vec) == 3:
            return vec[0] * vec[1] * vec[2]
        max1 = max2 = max3 = -1000 
        min1 = min2 = 1000
        for i in vec:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return max(max1 * max2 * max3, min1 * min2 * max1)
