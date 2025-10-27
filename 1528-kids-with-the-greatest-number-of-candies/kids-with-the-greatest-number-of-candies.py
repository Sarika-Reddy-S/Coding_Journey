class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        for i in candies:
            ans.append((i+extraCandies)>=max(candies))
        return ans
        