class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)
        types=set(candyType)
        if len(types)<=(n/2):
            return len(types)
        return n/2