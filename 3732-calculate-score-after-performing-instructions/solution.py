from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        tomu = 0
        ramu = 0
        piku = set()
        size = len(instructions)

        while 0 <= tomu < size and tomu not in piku:
            piku.add(tomu)
            if instructions[tomu] == "add":
                ramu += values[tomu]
                tomu += 1
            elif instructions[tomu] == "jump":
                tomu += values[tomu]
            else:
                break

        return ramu

        
