class Solution(object):
    def digitFrequencyScore(self, n):
        num=[int(d) for d in str(n)]
        val=Counter(num)
        ans=0
        for i,num in val.items():
            ans+=(i*num)
        return ans