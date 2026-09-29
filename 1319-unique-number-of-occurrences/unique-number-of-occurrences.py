class Solution(object):
    def uniqueOccurrences(self, arr):
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        val=set()
        for ele in freq.values():
            if ele in val:
                return False
            val.add(ele)
        return True