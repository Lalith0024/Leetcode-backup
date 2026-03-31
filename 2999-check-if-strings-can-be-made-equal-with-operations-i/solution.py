class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        # given string 1 , stirng 2 both of length 4, lowercase ->input

        # applicable ops:

        # 1) choose any 2 index -> i,j such that j-i=2 then swap the index of characters at those indices 
        # output cond -> if s1 == s2: return TRUE ELSE FALSE 

        # j-i=2, ((2,4),(1,3),(0,2))

        # hint ->. just go with brute force approach make sure your not including the case 0,2 only 2,4 and 1,3

        # ops 1 
        l1 = list(s1)
        l2 = list(s2)

        if l1 == l2:
            return True
        l1[0],l1[2] = l1[2],l1[0]
        if l1 == l2:
            return True

        l1[1],l1[3] = l1[3],l1[1]
        if l1 == l2:
            return True
        
        l2[0],l2[2] = l2[2],l2[0]
        if l1 == l2:
            return True
        
        l2[1],l2[3] = l2[3],l2[1]
        if l1 == l2:
            return True


        return False
