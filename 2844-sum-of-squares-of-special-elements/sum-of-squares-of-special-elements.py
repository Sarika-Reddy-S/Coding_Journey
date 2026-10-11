class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        val=0
        for i in range(n):
            index = i + 1
            if n%index==0:
                val+=(nums[i]**2)
        return val