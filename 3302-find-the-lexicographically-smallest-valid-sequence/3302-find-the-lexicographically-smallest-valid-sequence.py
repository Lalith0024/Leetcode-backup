
from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        n, m = len(word1), len(word2)
        suf = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j
        
        i = 0
        j = 0
        used_change = False
        result = []
        
        while j < m and i < n:

            if word1[i] == word2[j]:
                result.append(i)
                i += 1
                j += 1

            else:

                if not used_change and suf[i + 1] >= m - (j + 1):
                    result.append(i)
                    used_change = True
                    i += 1
                    j += 1
                    
                else:
                    i += 1
        
        if j == m:
            return result
        return []