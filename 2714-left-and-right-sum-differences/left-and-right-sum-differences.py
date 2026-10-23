class Solution(object):
    def leftRightDifference(self, nums):
        right=[]
        left=[]
        if len(nums)==1:
            right.append(0)
            return right
        for i in range(len(nums)-1):
            if i ==0:
                left.append(0)
            left.append(left[i]+nums[i])
        nums1 = nums[::-1]
        for i in range(len(nums1)-1):
            if i ==0:
                right.append(0)
            right.append(right[i]+nums1[i])
        diff=[]
        right=right[::-1]
        for i in range(len(left)):
            diff.append(abs(left[i]-right[i]))
        return diff