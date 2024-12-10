class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth>maxi:
                maxi = customer_wealth
        return maxi
        
