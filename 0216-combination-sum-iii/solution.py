class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def rec(k, n, i, temp):
            if n == 0 and len(temp) == k:   # ✅ valid combination
                ans.append(temp[:])
                return
            if n < 0 or len(temp) > k or i > 9:   # ✅ prune invalid paths
                return
            
            # choose i
            rec(k, n - i, i + 1, temp + [i])
            # skip i
            rec(k, n, i + 1, temp)
        
        rec(k, n, 1, [])
        return ans

