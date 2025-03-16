class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # def countGoodNumbers(n):
        MOD = 10**9 + 7
        
        # Even indices (0, 2, 4, ...): Can be {0, 2, 4, 6, 8} (5 choices)
        # Odd indices (1, 3, 5, ...): Can be {2, 3, 5, 7} (4 choices)
        
        even_count = (n + 1) // 2  # Count of even-indexed positions
        odd_count = n // 2         # Count of odd-indexed positions
        
        # Compute (5^even_count * 4^odd_count) % MOD efficiently using modular exponentiation
        def power(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:  # If exponent is odd, multiply base
                    result = (result * base) % mod
                base = (base * base) % mod  # Square the base
                exp //= 2
            return result
        
        return (power(5, even_count, MOD) * power(4, odd_count, MOD)) % MOD

            
