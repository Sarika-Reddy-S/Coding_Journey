class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        if target in nums:
            a=(nums.index(target))
        else:
            for i in nums:
                if i<=target:
                    a=(nums.index(i)+1)
        return (a)
                        