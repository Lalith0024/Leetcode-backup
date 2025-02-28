class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        all = []
        for i in accounts:
            all.append(sum(i))
        return max(all)

        
        
