class Solution(object):
    def uniqueOccurrences(self, arr):
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        val=[]
        for ele in freq.values():
            if ele in val:
                return False
            val.append(ele)
        return True