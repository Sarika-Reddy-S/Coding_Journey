class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        r=len(numbers)-1
        while left<r:
            total=numbers[left]+numbers[r]
            if total<target:
                left+=1
            elif total==target:
                return left+1,r+1
            else:
                r-=1  