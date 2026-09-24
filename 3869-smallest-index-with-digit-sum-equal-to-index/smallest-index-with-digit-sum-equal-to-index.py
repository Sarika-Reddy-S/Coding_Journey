class Solution(object):
    def smallestIndex(self, nums):
        for i,n in enumerate(nums):
            if i==sum(map(int,str(n))):
                return i
        return -1
        