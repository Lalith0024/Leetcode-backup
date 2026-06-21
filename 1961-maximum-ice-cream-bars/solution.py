class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Sort in ascending order to buy the cheapest bars first
        costs.sort() 
        
        c = 0
        temp = 0
        for i in costs:
            # Exceed, break
            if temp + i > coins:
                break
            if temp == coins:
                return c
            
            temp += i
            c += 1
            
        return c
