from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s=s1.split()+s2.split()
        ans=[]
        for val,key in Counter(s).items():
            if key<2:
                ans.append(val)
        return (ans)