class Solution(object):
    def findMissingElements(self, nums):
        val=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                val.append(i)
        return val
        