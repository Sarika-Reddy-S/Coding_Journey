class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums[i] in nums[(i+1):]:
                a.append(nums[i])
        return a