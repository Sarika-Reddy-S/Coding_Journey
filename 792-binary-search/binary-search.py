class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=-1
        if target in nums:
            return nums.index(target)
        else:
            return a