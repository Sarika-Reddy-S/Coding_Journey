class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c+=1
            ans.append(c)
        return (ans)