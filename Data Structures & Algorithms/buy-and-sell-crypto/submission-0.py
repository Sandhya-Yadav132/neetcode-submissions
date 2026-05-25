class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini_price=prices[0]
        max_profit=0
        for price in prices:
            mini_price=min(mini_price,price)
            current_profit=price-mini_price
            max_profit=max(current_profit,max_profit)
        return max_profit
