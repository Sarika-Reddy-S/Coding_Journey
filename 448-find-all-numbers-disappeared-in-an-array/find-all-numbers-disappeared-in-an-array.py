class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        a=set(nums)
        val=[]
        for i in range(len(nums)):
            if i+1 not in a:
                val.append(i+1)
        return val
        