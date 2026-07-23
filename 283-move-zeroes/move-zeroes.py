class Solution(object):
    def moveZeroes(self, nums):
        stack=[]
        lst1=[]
        for i in nums:
            if i!=0:
                stack.append(i)
            else:
                lst1.append(i)
        nums[:]=stack+lst1
        return nums 