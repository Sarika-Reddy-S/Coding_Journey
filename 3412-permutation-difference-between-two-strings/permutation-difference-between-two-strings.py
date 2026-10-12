class Solution(object):
    def findPermutationDifference(self, s, t):
        val=0
        for i in range(len(s)):
            if s[i] in t:
                ans=t.index(s[i])
                val+=abs(ans-i)
        return val