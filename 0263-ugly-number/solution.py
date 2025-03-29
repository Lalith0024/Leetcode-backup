class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<=0:
            return False
        # lst = [2,3,5]
        # for i in lst:
        #     while n%i==0: #first checiking if divisible by either 2 or 3 or 5 
        #         n = i//n 
        # return n==1        #this indicates wheater the number is not divisible by any other number execpt 2 or 3 or 5 


        #easy way 
        while n%2==0:
            n = n//2
        while n%3==0:
            n = n//3
        while n%5 ==0:
            n = n//5
        return n==1
