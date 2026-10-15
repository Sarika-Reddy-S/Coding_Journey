class Solution(object):
    def sumCounts(self, nums):
        val=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                val+=(len(set(nums[i:j]))**2)
        return val
        