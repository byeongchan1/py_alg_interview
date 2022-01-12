# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        # max_value = prices[0]
        high_profit = 0
        
        for n in prices:
            
            if min_value > n:
                min_value = n
                # max_value = n
            
            if high_profit < (n - min_value):
                high_profit = n - min_value
                # max_value = n
        
        return high_profit
            