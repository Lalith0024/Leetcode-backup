class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        # Initialize the maximum profit to 0 (no profit is better than a loss)
        max_profit = 0
        
        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the potential profit if we sold at the current price
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit
            
