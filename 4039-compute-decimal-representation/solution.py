class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        pos = 1

        while n>0:
            digi = n%10
            # here we should first handle the digit not equal to 0 things.. 
            if digi!=0:
                ans.append(digi*pos)
            # yo dont get stuck in the loop reduce the digit.. 
            n = n//10
            pos *= 10

        ans.sort(reverse = True)
        return ans
                
            
        
