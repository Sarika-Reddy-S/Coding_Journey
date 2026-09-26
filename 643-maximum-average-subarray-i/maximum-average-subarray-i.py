class Solution(object):
    def findMaxAverage(self, nums, k):
        wind_siz=sum(nums[:k])
        mx_val=wind_siz
        for i in range(k,len(nums)):
            wind_siz+=nums[i]
            wind_siz-=nums[i-k]
            mx_val=max(mx_val,wind_siz)
        return float(mx_val)/k
        