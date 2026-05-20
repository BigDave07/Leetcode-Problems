class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = Buy and right = Sell
        max_profit = 0;

        while r < len(prices):
            if prices[l] < prices[r]:  #Profitable
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r #Move left pointer to right pointer
            r += 1 #Move right pointer to the right

        return max_profit
    
# Time complexity: O(n)
# Space complexity: O(1)
 