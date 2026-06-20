def findspot(diff  , l  , r):
    i = 0
    j = 10**9
    ans = -1
    while i <= j:
        mid = (i + j ) // 2
        steps = mid - l
        remain = diff - steps
        val = abs(mid - r) 
        if remain >= val:
            ans = mid
            i = mid + 1
        else:
            j = mid - 1
    return ans


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len( restrictions ) == 0:return n - 1
        restrictions.sort()
        m = len(restrictions)
        store = {}
        currpt = 1
        currht = 0
        for id , ht in restrictions:
            diff = id - currpt
            projht = currht + diff
            projht = min( projht , ht )
            store[id] = projht
            currht = projht
            currpt = id
        
        store[restrictions[-1][0]] = min(restrictions[-1][1] , store[restrictions[-1][0]] )
        currpt , currht = restrictions[-1]
    
        for i in range( m - 2 , -1 , -1):
            id , ht = restrictions[i]
            diff = currpt - id
            projht = currht + diff
            projht = min( projht , ht )
            store[id] = min( store[id] , projht)
            currpt = id
            currht = min( store[id] , projht)

        maxht = 0
        currht = 0
        currpt = 1
        for id , ht in restrictions:
            h = store[id]
            maxht = max( maxht , findspot(id - currpt  , currht  , h))
            currpt = id
            currht = store[id]
        maxht = max( maxht , currht + n - currpt)
        return maxht
