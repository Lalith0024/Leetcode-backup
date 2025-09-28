class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r-l+1
        sorn = (n,l,r)
       # they told to take mod make sure take it and use else testcase wont work.. 
        mod = (10**9)+7
        # initalize dps arrayss raa
        dp_dow = [1]*m
        dp_up = [1]*m
        for _ in range(2, n + 1): 
            new_up = [0] * m 
            new_down = [0] * m

            pref_up = [0]*(m+1)
            pref_dow = [0]* (m+1)
            for i in range(m):
                pref_up[i+1] = (pref_up[i] + dp_up[i]) % mod
                pref_dow[i+1] = (pref_dow[i] + dp_dow[i]) % mod

            for k in range(m):
                new_up[k] = pref_dow[k] % mod 
                new_down[k] = (pref_up[m] - pref_up[k + 1]) % mod

            dp_up, dp_dow = new_up, new_down
        return (sum(dp_up) + sum(dp_dow)) % mod
                
