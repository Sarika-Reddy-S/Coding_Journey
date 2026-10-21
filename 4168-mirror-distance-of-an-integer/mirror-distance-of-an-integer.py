class Solution(object):
    def mirrorDistance(self, n):
        val=str(n)
        return abs(n-int(val[::-1]))