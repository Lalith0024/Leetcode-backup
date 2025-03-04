class Solution(object):
    def rob(self, nums):
        return reduce(lambda q,v:(q[1],max(q[0]+v,q[1])),nums,(0,0))[1]
        
