class Solution(object):
    def moveZeroes(self, nums):
        uniq=0
        for current in range(len(nums)):
            if nums[current]!=0:
                nums[uniq],nums[current]=nums[current],nums[uniq]
                uniq+=1
        return nums