class Solution(object):
    def majorityElement(self, nums):
        target=len(nums)/3
        freq={}
        val=set()
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in nums:
            if freq[i]>target:
                val.add(i)
        return list(val)
        