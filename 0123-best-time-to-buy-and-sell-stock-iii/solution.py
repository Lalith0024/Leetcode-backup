class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize the states
        firstBuy = float('-inf')
        firstSell = 0
        secondBuy = float('-inf')
        secondSell = 0

        # Iterate through each price
        for price in prices:
            # Update states
            firstBuy = max(firstBuy, -price)  # Max profit after the first buy
            firstSell = max(firstSell, firstBuy + price)  # Max profit after the first sell
            secondBuy = max(secondBuy, firstSell - price)  # Max profit after the second buy
            secondSell = max(secondSell, secondBuy + price)  # Max profit after the second sell

        # Return the maximum profit after the second sell
        return secondSell
        
