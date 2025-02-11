class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power(n):
            if n==1:
                return True
            if n < 1 or n % 2 != 0:
                return False
            return power(n//2)
            
        return power(n)

