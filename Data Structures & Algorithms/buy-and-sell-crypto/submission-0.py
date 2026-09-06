class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Left and right pointer
        l, r = 0, 1 #Left = buy, right = sell
        maxP = 0 #to track max profit

        while r < len(prices): #while r is within the array
            #profitable ?
            if prices[l] < prices[r]: #if prices[r] > prices[l] compute the profit and update maxP
                profit = prices[r] - prices[l] 
                maxP = max(maxP, profit)
            else:
                l = r #move 1 to r cause we found a cheaper buy price
            r += 1 #move r to the next day

        return maxP