class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # string based 
        # text: "balloon"
        dic = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i == 'b':
                dic['b']+=1
            if i == 'a':
                dic['a']+=1
            if i == 'l':
                dic['l']+=1
            if i == 'o':
                dic['o']+=1
            if i == 'n':
                dic['n']+=1


        # we have got the count we used hashmap to store the counts now, 
        # hint : dividde the l, o with integer and check the instances 

        dic['l'] //= 2
        dic['o'] //= 2
        # safey check
        for i,j in dic.items():
            if j!=0:
                continue 
            else:
                return 0
        # we dont care about extras to only return the existance
        return min(dic.values())

    
            
        
                
            
            
