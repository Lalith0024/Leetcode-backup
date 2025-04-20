from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        dora = []
        for nobita in nums:
            while dora and dora[-1] > nobita:
                x = dora.pop()
                nobita = max(nobita, x)
            dora.append(nobita)
        return len(dora)

