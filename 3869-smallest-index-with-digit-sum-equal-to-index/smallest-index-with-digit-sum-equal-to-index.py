class Solution(object):
    def smallestIndex(self, nums):
        ans=-1
        for i in range(len(nums)):
            if sum(int(s) for s in str(nums[i]))==i:
                ans=i
                break
        return ans
        