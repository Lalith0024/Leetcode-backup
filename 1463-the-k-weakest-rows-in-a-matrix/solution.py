class Solution(object):
    def kWeakestRows(self, mat, k):
        def count(new):
            l = 0
            r = len(new)-1
            while l<=r:
                m = (l+r)//2
                if new[m]==1:
                    l =m+1
                else:
                    r = m-1
            return l 
        newly = [[count(mat[x]),x] for x in range(len(mat))]
        newly.sort()
        return([i for _,i in newly[:k]])
        
