class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        for i in candies:
            if (i+extraCandies)>=max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        