class Solution(object):
    def intersect(self, nums1, nums2):
        freq1={}
        result=[]
        for i in nums1:
            freq1[i]=freq1.get(i,0)+1
        for i in nums2:
            if freq1.get(i,0)>0:
                result.append(i)
                freq1[i]-=1
        return result