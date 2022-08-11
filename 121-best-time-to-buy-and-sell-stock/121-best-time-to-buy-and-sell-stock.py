class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1 
        max_profit = 0
        #having a cursor at left and right 
        #left is for buying and right is for sellling
        #generating different profits and moving the cursor
        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit