class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        def check(k,piles,h):
            total = 0
            for i in range(len(piles)):
                total +=piles[i]//k
                if piles[i]%k!=0:
                    total+=1
            return total<=h


        while start<=end:
            mid = (start+end)//2
            if check(mid,piles,h):
                min_ans = mid
                end = mid-1
            else:
                start = mid+1

        return min_ans
            
