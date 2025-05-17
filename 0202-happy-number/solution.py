class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        while True:
            if n==1:
                return True #great method 
           
            sum=0
            while n!=0:
                digit=n%10
                sum+=digit*digit
                n=n//10
                
            n=sum
            if n not in l:
                l.add(n)
            else:
                return False
            
