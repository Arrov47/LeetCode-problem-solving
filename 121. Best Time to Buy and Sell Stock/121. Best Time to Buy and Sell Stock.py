class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # give the first element for initial value
        buy = prices[0]
        sell = prices[0]
        bestDeal = sell-buy


        for price in prices:
            if price < buy: # buy stock if its price is lower than previous one's
                buy = price 
                sell = price # since we can only sell after buying, 
                             # our sell price must be the the same as buy price or come after it

            elif price > sell:
                sell = price # we want to sell stock for a price which is as high as possible

            if bestDeal < sell-buy: # we must track the maximum profits we can make,
                bestDeal = sell-buy # and pick up the highest one

        return bestDeal
        

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(prices))