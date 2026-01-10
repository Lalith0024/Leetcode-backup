class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            c = 0
            sums = 0
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    if j == i // j:
                        c += 1
                        sums += j
                    else:
                        c += 2
                        sums += j + i // j
                if c > 4:
                    break
            if c == 4:
                ans += sums
        return ans

            

