class Solution(object):
    def maximumDifference(self, nums):
        max_val=-1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    a=(nums[j]-nums[i])
                    max_val=max(max_val,a)
        return (max_val)