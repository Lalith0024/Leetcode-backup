def fwht(a):
    n,h,ans = len(a), 1, a[:]
    while h < n:
        for i in range(0, n, h << 1):
            for j in range(i, i + h):
                ans[j],ans[j+h] = (x:=ans[j]) + (y:=ans[j+h]), x - y
        h <<= 1
    return  ans

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        freq = [0]*(1 << max(nums).bit_length())
        for num in nums: freq[num] += 1
        return  sum(1 for c in fwht([x**3 for x in fwht(freq)]) if c)
        