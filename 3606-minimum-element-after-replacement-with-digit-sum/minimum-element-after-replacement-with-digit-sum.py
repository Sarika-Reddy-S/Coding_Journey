class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for n in range(len(nums)):
            a=str(nums[n])
            if len(a)<=1:
                arr.append(min(nums))
            else:
                s = 0
                for i in a:
                    s += int(i)    # Add each digit
                arr.append(s) 
        nums=arr
        return(min(nums))