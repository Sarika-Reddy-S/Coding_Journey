class Solution(object):
    def findPermutationDifference(self, s, t):
        val=0
        for i in range(len(s)):
            val=val+abs(t.find(s[i])-i)
        return val