class Solution(object):
    def containsDuplicate(self, nums):
        seen={}
        for i in nums:
            if i in seen:
                return True
            seen[i]=seen.get(i,0)+1
        return False
        