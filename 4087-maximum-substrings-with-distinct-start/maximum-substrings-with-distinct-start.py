class Solution:
    def maxDistinct(self, s: str) -> int:
        result={}
        for i in s:
            result[i]=result.get(i,0)+1
        return len(result)