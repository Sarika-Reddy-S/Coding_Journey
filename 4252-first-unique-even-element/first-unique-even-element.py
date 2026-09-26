class Solution(object):
    def firstUniqueEven(self, nums):
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for s in range(len(nums)):
            if freq[nums[s]]==1 and nums[s]%2==0:
                return (nums[s])
        return -1