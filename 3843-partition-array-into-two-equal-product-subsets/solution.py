from typing import List
from itertools import combinations
from math import prod

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(1, n):
            for golu in combinations(range(n), i):
                molu = [nums[j] for j in golu]
                polu = [nums[j] for j in range(n) if j not in golu]
                if not polu:
                    continue
                if prod(molu) == target and prod(polu) == target:
                    return True
        return False

