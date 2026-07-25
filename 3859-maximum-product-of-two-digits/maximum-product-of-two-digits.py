class Solution(object):
    def maxProduct(self, n):
        digit=[int(d) for d in str(n)]
        digit.sort()
        return (digit[-1]*digit[-2])
        