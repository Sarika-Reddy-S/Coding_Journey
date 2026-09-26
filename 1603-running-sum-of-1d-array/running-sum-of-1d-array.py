class Solution(object):
    def runningSum(self, nums):
        nums.reverse()
        ans=[]
        for i in range(len(nums)):
            ans.append(sum(nums[i:len(nums)]))
        ans.reverse()
        return ans
        