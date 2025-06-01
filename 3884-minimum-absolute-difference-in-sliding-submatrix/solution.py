from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ramu = []
        for i in range(m - k + 1):
            chintu = []
            for j in range(n - k + 1):
                nomu = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        nomu.add(grid[x][y])
                babu = sorted(nomu)
                if len(babu) <= 1:
                    chintu.append(0)
                else:
                    minu = float('inf')
                    for z in range(1, len(babu)):
                        minu = min(minu, babu[z] - babu[z - 1])
                    chintu.append(minu)
            ramu.append(chintu)
        return ramu

