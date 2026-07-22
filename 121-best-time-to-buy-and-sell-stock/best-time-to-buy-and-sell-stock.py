class Solution(object):
    def maxProfit(self, prices):
        mins=float('inf')
        maxs=0
        for i in range(len(prices)):
            if prices[i] < mins:
                mins=prices[i]
            else:
                maxs=max(prices[i]-mins,maxs)
        return (maxs)
        